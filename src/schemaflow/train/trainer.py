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

def compute_db_loss(policy, trajectories, encode_batch_size=8):
    items = []
    schema_lookup, query_lookup = {}, {}

    for traj_idx, traj in enumerate(trajectories):
        schema = SCHEMAS[traj.example["schema"]]
        schema_lookup[traj_idx] = schema
        query_lookup[traj_idx] = traj.query

        for step in traj.steps:
            for s in (step.state, step.next_state):
                if s.is_terminal:
                    continue
                key = (traj_idx, s)
                items.append(key)

    if not items:
        return torch.zeros((), device=policy.device, requires_grad=True)

    outputs = policy.batch_forward(items, schema_lookup, query_lookup, encode_batch_size)

    all_residuals = []
    for traj_idx, traj in enumerate(trajectories):
        for step in traj.steps:
            out_s = outputs[(traj_idx, step.state)]
            action_idx = out_s.actions.index(step.action)
            log_pf = out_s.log_probs[action_idx]
            log_f_s = out_s.log_flow

            if step.next_state.is_terminal:
                log_f_s_next = torch.zeros_like(log_f_s)
            else:
                log_f_s_next = outputs[(traj_idx, step.next_state)].log_flow

            log_pb = torch.as_tensor(step.log_p_b, device=log_f_s.device, dtype=log_f_s.dtype)
            all_residuals.append((log_f_s + log_pf) - (log_f_s_next + log_pb))

    residuals = torch.stack(all_residuals)
    return (residuals ** 2).mean()

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

        self.train_dataset = SchemaLinkingDataset(config.training.train_data, max_trajectories=None)
        self.val_dataset = SchemaLinkingDataset(config.training.eval_data, max_trajectories=None)
        self.test_dataset = SchemaLinkingDataset(config.training.test_data, max_trajectories=None)
        
        print(f"Loaded train_dataset with samples: {len(self.train_dataset)}")
        print(f"Loaded val_dataset with samples: {len(self.val_dataset)}")
        print(f"Loaded test_dataset with samples: {len(self.test_dataset)}")

        self.optimizer = self._build_optimizer()
        self.reward_fn = SchemaLinkingReward(config.reward, device=self.device)

        self.global_step = 0
        self.examples_seen = 0
        self.transitions_seen = 0
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
    def train_step(self, policy, trajectories, optimizer, grad_clip, encode_batch_size=8):
        """Training wrapper: computes loss, backprops, and steps the optimizer."""
        optimizer.zero_grad()
        loss = compute_db_loss(policy, trajectories, encode_batch_size)
        loss.backward()
        torch.nn.utils.clip_grad_norm_(policy.trainable_parameters(), grad_clip)
        optimizer.step()
        return loss.item()
    
    def train(self) -> None:
        trainable = sum(p.numel() for p in self.policy.parameters() if p.requires_grad)
        total = sum(p.numel() for p in self.policy.parameters())

        print(f"Trainable: {trainable:,} / {total:,}")
        
        cfg = self.config.training
        self.policy.train()

        for epoch in range(cfg.num_epochs):
            print(f"[train] epoch {epoch+1}")
            print(f"[train] train dataset size: {len(self.train_dataset)}")
            indices = list(range(len(self.train_dataset)))
            if getattr(cfg, "shuffle", True):
                random.shuffle(indices)

            batch_size = getattr(cfg, "train_batch_size", 8)
            for start in tqdm(range(0, len(indices), batch_size), desc="Training"):
                batch_idx = indices[start : start + batch_size]
                batch = [self.train_dataset[i] for i in batch_idx]

                loss = self.train_step(self.policy, batch, self.optimizer, cfg.grad_clip)

                # print(
                #     torch.cuda.memory_allocated() / 1024**3,
                #     torch.cuda.memory_reserved() / 1024**3,
                # )

                self.global_step += 1
                self.examples_seen += len(batch)
                self.transitions_seen += sum(len(t.steps) for t in batch)
                
                if self.global_step % getattr(cfg, "log_every", 50) == 0:
                    print(f"epoch {epoch} | step {self.global_step} | loss {loss:.4f}")
                    print(f"Trajectories seen: {self.examples_seen}")
                    print(f"Transitions seen: {self.transitions_seen}")

            metrics = self.evaluate(split="val")
            self.save_checkpoint()
            self.save_best_checkpoint(metrics)
        
        print("\nTraining complete.")
        print("Evaluating on test set using final model...")
        
        best_ckpt = torch.load(
            os.path.join(self.config.training.output_dir, "checkpoint_best.pt"),
            map_location=self.device,
        )

        self.policy.load_state_dict(best_ckpt["model"])

        test_metrics = self.evaluate(
            dataset=self.test_dataset,
            split="test",
        )

        print(f"Final test metrics: {test_metrics}")

    # ------------------------------------------------------------------
    @torch.no_grad()
    def evaluate(
        self,
        dataset: SchemaLinkingDataset | None = None,
        split: str = "val",
    ) -> dict:
        self.policy.eval()

        dataset = dataset or self.val_dataset

        total_loss = 0.0
        total_reward = 0.0
        n_batches = 0
        n_examples = 0

        print(f"[{split}] dataset size: {len(dataset)}")

        eval_batch_size = getattr(self.config.training, "eval_batch_size", 8)
        indices = list(range(len(dataset)))

        for start in tqdm(
            range(0, len(indices), eval_batch_size), desc=f"Evaluating ({split})"
        ):
            batch_idx = indices[start : start + eval_batch_size]
            batch = [dataset[i] for i in batch_idx]

            loss = compute_db_loss(self.policy, batch, encode_batch_size=8)
            total_loss += loss.item()
            n_batches += 1

            for traj in batch:
                schema = SCHEMAS[traj.example["schema"]]
                terminal_state = self.policy.rollout(traj.query, schema, greedy=True)

                if terminal_state.is_terminal:
                    reward = self.reward_fn(
                        terminal_state,
                        schema,
                        gold_nodes=frozenset(traj.example["gold"]["nodes"]),
                        gold_node_props=frozenset(traj.example["gold"]["node_props"]),
                        gold_rels=frozenset(traj.example["gold"]["relations"]),
                        gold_rel_props=frozenset(
                            traj.example["gold"]["relation_props"]
                        ),
                    )
                else:
                    reward = 0.0

                total_reward += reward
                n_examples += 1

        self.policy.train()

        metrics = {
            f"{split}_loss": total_loss / max(n_batches, 1),
            f"{split}_reward": total_reward / max(n_examples, 1),
        }

        print(
            f"[{split}] step {self.global_step} "
            f"loss={metrics[f'{split}_loss']:.4f} "
            f"reward={metrics[f'{split}_reward']:.4f}"
        )

        return metrics

    # ------------------------------------------------------------------
    def save_checkpoint(self, tag: str = None) -> str:
        cfg = self.config.training
        os.makedirs(cfg.output_dir, exist_ok=True)

        name = tag or f"checkpoint_step{self.global_step}.pt"
        path = os.path.join(cfg.output_dir, name)

        torch.save(
            {
                "model": self.policy.state_dict(),
                "optimizer": self.optimizer.state_dict(),
                "step": self.global_step,
                "config": self.config,
            },
            path,
        )

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
            torch.save(
                {
                    "model": self.policy.state_dict(),
                    "optimizer": self.optimizer.state_dict(),
                    "step": self.global_step,
                    "val_reward": metrics["val_reward"],
                    "val_loss": metrics["val_loss"],
                },
                path,
            )
            print(
                f"[checkpoint] new best val_reward={metrics['val_reward']:.4f}, saved to {path}"
            )


if __name__ == "__main__":
    trainer = Trainer(DEFAULT_CONFIG)
    trainer.train()
