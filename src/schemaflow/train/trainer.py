from __future__ import annotations

import os
import random
from typing import List
from tqdm import tqdm

import torch
from schemaflow.config import Config, DEFAULT_CONFIG

from schemaflow.policy.model import SchemaFlowPolicy
from schemaflow.data.dataset import SchemaLinkingDataset, Trajectory
from schemaflow.data.schemas import SCHEMAS
from schemaflow.reward.reward import SchemaLinkingReward
from schemaflow.schema.state import SchemaState

# ──────────────────────────────────────────────────────────────────────
# Detailed balance loss
# ──────────────────────────────────────────────────────────────────────


def compute_db_loss(
    policy: SchemaFlowPolicy,
    trajectories: List[Trajectory],
) -> torch.Tensor:

    all_residuals = []

    for traj in tqdm(trajectories, desc="Computing DB Loss"):
        schema = SCHEMAS[traj.example["schema"]]
        state_cache: dict = {}

        def get_out(s: SchemaState):
            if s not in state_cache:
                state_cache[s] = policy(s, schema, traj.query)
            return state_cache[s]

        for step in traj.steps:
            out_s = get_out(step.state)

            action_idx = out_s.actions.index(step.action)
            log_pf = out_s.log_probs[action_idx]
            log_f_s = out_s.log_flow

            if step.next_state.is_terminal:
                log_f_s_next = torch.zeros_like(log_f_s)  # log(reward=1.0) == 0
            else:
                out_s_next = get_out(step.next_state)
                log_f_s_next = out_s_next.log_flow
            
            log_pb = torch.as_tensor(step.log_p_b, device=log_f_s.device, dtype=log_f_s.dtype)

            residual = (log_f_s + log_pf) - (log_f_s_next + log_pb)
            all_residuals.append(residual)

    if not all_residuals:
        return torch.zeros((), device=policy.device, requires_grad=True)
    
    residuals = torch.stack(all_residuals)
    return (residuals**2).mean()


# ──────────────────────────────────────────────────────────────────────
# Trainer
# ──────────────────────────────────────────────────────────────────────


class Trainer:
    def __init__(self, config: Config = DEFAULT_CONFIG):
        torch.manual_seed(config.training.seed)
        random.seed(config.training.seed)
        
        self.config = config
        self.device = config.device

        self.policy = SchemaFlowPolicy(
            model_config=config.model,
            lora_config=config.lora,
            gfn_config=config.gfn,
            device=self.device,
        ).to(self.device)
        self.policy = self.policy.to(self.policy.llm.model.dtype)

        self.train_dataset = SchemaLinkingDataset(config.training.train_data)
        self.val_dataset = SchemaLinkingDataset(config.training.eval_data)

        self.optimizer = self._build_optimizer()
        self.reward_fn = SchemaLinkingReward(config.reward, device=self.device)
        
        self.global_step = 0
        self.best_val_reward = float("-inf")

    # ------------------------------------------------------------------
    def _build_optimizer(self) -> torch.optim.Optimizer:
        params = (
            [p for p in self.policy.llm.model.parameters() if p.requires_grad]
            + list(self.policy.policy_head.parameters())
            + list(self.policy.flow_head.parameters())
        )
        return torch.optim.AdamW(params, lr=self.config.training.lr)

    # ------------------------------------------------------------------
    def train(self) -> None:
        cfg = self.config.training
        self.policy.train()

        for epoch in range(cfg.num_epochs):
            print(f"[train] epoch {epoch}")
            print(f"[train] train dataset size: {len(self.train_dataset)}")
            indices = list(range(len(self.train_dataset)))
            if getattr(cfg, "shuffle", True):
                random.shuffle(indices)

            batch_size = getattr(cfg, "train_batch_size", 8)
            for start in tqdm(range(0, len(indices), batch_size), desc="Training"):
                batch_idx = indices[start:start + batch_size]
                batch = [self.train_dataset[i] for i in batch_idx]

                loss = compute_db_loss(self.policy, batch)

                self.optimizer.zero_grad()
                loss.backward()
                torch.nn.utils.clip_grad_norm_(self.policy.trainable_parameters(), cfg.grad_clip)
                self.optimizer.step()
                
                print(
                    torch.cuda.memory_allocated() / 1024**3,
                    torch.cuda.memory_reserved() / 1024**3,
                )

                self.global_step += 1
                if self.global_step % getattr(cfg, "log_every", 50) == 0:
                    print(f"epoch {epoch} step {self.global_step} loss {loss.item():.4f}")

            
            metrics = self.evaluate()
            self.save_checkpoint()
            self.save_best_checkpoint(metrics)
            
    # ------------------------------------------------------------------
    @torch.no_grad()
    def evaluate(self) -> dict:
        self.policy.eval()

        total_loss = 0.0
        total_reward = 0.0
        n_batches = 0
        n_examples = 0

        print(f"[eval] val dataset size: {len(self.val_dataset)}")
        eval_batch_size = getattr(self.config.training, "eval_batch_size", 8)
        indices = list(range(len(self.val_dataset)))

        for start in tqdm(range(0, len(indices), eval_batch_size), desc="Evaluating"):
            batch_idx = indices[start:start + eval_batch_size]
            batch = [self.val_dataset[i] for i in batch_idx]

            loss = compute_db_loss(self.policy, batch)
            total_loss += loss.item()
            n_batches += 1

            for traj in batch:
                schema = SCHEMAS[traj.example["schema"]]
                terminal_state = self.policy.rollout(traj.query, schema, greedy=True)
                if terminal_state.is_terminal:
                    reward = self.reward_fn(
                        terminal_state, schema,
                        gold_nodes=frozenset(traj.example["gold"]["nodes"]),
                        gold_node_props=frozenset(traj.example["gold"]["node_props"]),
                        gold_rels=frozenset(traj.example["gold"]["relations"]),
                        gold_rel_props=frozenset(traj.example["gold"]["relation_props"]),
                    )
                else:
                    reward = 0.0
                
                total_reward += reward
                n_examples += 1
        
        self.policy.train()

        metrics = {
            "val_loss": total_loss / max(n_batches, 1),
            "val_reward": total_reward / max(n_examples, 1),
        }
        print(f"[eval] step {self.global_step} loss={metrics['val_loss']:.4f} "
            f"reward={metrics['val_reward']:.4f}")
        return metrics

    # ------------------------------------------------------------------
    def save_checkpoint(self, tag: str = None) -> str:
        cfg = self.config.training
        os.makedirs(cfg.output_dir, exist_ok=True)

        name = tag or f"checkpoint_step{self.global_step}.pt"
        path = os.path.join(cfg.output_dir, name)

        torch.save({
            "model": self.policy.state_dict(),
            "optimizer": self.optimizer.state_dict(),
            "step": self.global_step,
            "config": self.config,
        }, path)

        keep_last = getattr(cfg, "keep_last_n", 3)
        ckpts = sorted(
            [f for f in os.listdir(cfg.output_dir) if f.startswith("checkpoint_step")],
            key=lambda f: int(f.split("checkpoint_step")[1].split(".pt")[0]),
        )
        for old in ckpts[:-keep_last]:
            os.remove(os.path.join(cfg.output_dir, old))

        return path

    # ------------------------------------------------------------------
    def save_best_checkpoint(self, metrics: dict) -> None:
        if metrics["val_reward"] > self.best_val_reward:
            self.best_val_reward = metrics["val_reward"]
            cfg = self.config.training
            os.makedirs(cfg.output_dir, exist_ok=True)
            path = os.path.join(cfg.output_dir, "checkpoint_best.pt")
            torch.save({
                "model": self.policy.state_dict(),
                "optimizer": self.optimizer.state_dict(),
                "step": self.global_step,
                "val_reward": metrics["val_reward"],
                "val_loss": metrics["val_loss"],
            }, path)
            print(f"[checkpoint] new best val_reward={metrics['val_reward']:.4f}, saved to {path}")
            

if __name__ == "__main__":
    trainer = Trainer(DEFAULT_CONFIG)
    trainer.train()
