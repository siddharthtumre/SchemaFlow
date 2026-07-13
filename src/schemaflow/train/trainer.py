from __future__ import annotations

import os
import math
import random
from typing import List
from tqdm import tqdm

import torch
from transformers import get_cosine_schedule_with_warmup
from schemaflow.config import Config, DEFAULT_CONFIG

from schemaflow.policy.model import SchemaFlowPolicy
from schemaflow.data.dataset import SchemaLinkingDataset, Trajectory
from schemaflow.data.schemas import SCHEMAS
from schemaflow.reward.reward import SchemaLinkingReward
from schemaflow.schema.state import SchemaState

# ──────────────────────────────────────────────────────────────────────
# Detailed balance loss
# ──────────────────────────────────────────────────────────────────────

def compute_db_loss(policy, trajectories, encode_batch_size=64):
    items = []
    seen = set()
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
                if key not in seen:
                    seen.add(key)
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
        self.model_config = config.model

        self.policy = SchemaFlowPolicy(
            model_config=self.model_config,
            lora_config=config.lora,
            gfn_config=config.gfn,
        )
        
        if config.model.load_in_4bit:
            dtype = self.policy.llm.model.dtype

            self.policy.policy_head.to(device=self.device, dtype=dtype)
            self.policy.flow_head.to(device=self.device, dtype=dtype)
        else:
            self.policy.to(self.device)
            self.policy.to(dtype=self.policy.llm.model.dtype)

        self.train_dataset = SchemaLinkingDataset(config.training.train_data, max_trajectories=None)
        self.val_dataset = SchemaLinkingDataset(config.training.eval_data, max_trajectories=None)
        self.test_dataset = SchemaLinkingDataset(config.training.test_data, max_trajectories=None)
        
        print(f"Loaded train_dataset with samples: {len(self.train_dataset)}")
        print(f"Loaded val_dataset with samples: {len(self.val_dataset)}")
        print(f"Loaded test_dataset with samples: {len(self.test_dataset)}")

        self.optimizer = self._build_optimizer()
        self.scheduler = self._build_scheduler()
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
    
    def _build_scheduler(self):
        cfg = self.config.training
        batch_size = getattr(cfg, "train_batch_size", 8)
        steps_per_epoch = (len(self.train_dataset) + batch_size - 1) // batch_size
        total_steps = steps_per_epoch * cfg.num_epochs
        warmup_steps = int(0.06 * total_steps)

        return get_cosine_schedule_with_warmup(
            self.optimizer,
            num_warmup_steps=warmup_steps,
            num_training_steps=total_steps,
        )

    # ------------------------------------------------------------------
    def _iter_batches(self, dataset, batch_size, shuffle=False):
        indices = list(range(len(dataset)))
        if shuffle:
            random.shuffle(indices)
        for start in range(0, len(indices), batch_size):
            idx = indices[start : start + batch_size]
            yield [dataset[i] for i in idx]
    
    def train_step(self, policy, trajectories, optimizer, scheduler, grad_clip, encode_batch_size=64):
        """Training wrapper: computes loss, backprops, and steps the optimizer."""
        optimizer.zero_grad()
        loss = compute_db_loss(policy, trajectories, encode_batch_size)
        loss.backward()
        torch.nn.utils.clip_grad_norm_(policy.trainable_parameters(), grad_clip)
        optimizer.step()
        scheduler.step()
        return loss.item()
    
    def train(self) -> None:
        trainable = sum(p.numel() for p in self.policy.parameters() if p.requires_grad)
        total = sum(p.numel() for p in self.policy.parameters())

        print(f"Trainable: {trainable:,} / {total:,}")
        
        cfg = self.config.training
        self.policy.train()

        encode_batch_size = getattr(cfg, "encode_batch_size", 128)
        for epoch in range(cfg.num_epochs):
            print(f"[train] epoch {epoch+1}")
            print(f"[train] train dataset size: {len(self.train_dataset)}")

            train_batch_size = getattr(cfg, "train_batch_size", 8)
            shuffle = getattr(cfg, "shuffle", True)
            total_batches = math.ceil(len(self.train_dataset) / train_batch_size)
            for batch in tqdm(
                self._iter_batches(self.train_dataset, train_batch_size, shuffle),
                total=total_batches,
                desc="Training",
            ):
                loss = self.train_step(self.policy, batch, self.optimizer, self.scheduler, cfg.grad_clip, encode_batch_size=encode_batch_size)

                self.global_step += 1
                self.examples_seen += len(batch)
                self.transitions_seen += sum(len(t.steps) for t in batch)
                
                if self.global_step % getattr(cfg, "log_every", 50) == 0:
                    print(f"epoch {epoch} | step {self.global_step} | loss {loss:.4f} | lr {self.scheduler.get_last_lr()[0]:.2e}")
                    print(f"Trajectories seen: {self.examples_seen}")
                    print(f"Transitions seen: {self.transitions_seen}")

                if self.global_step % getattr(cfg, "eval_every", 200) == 0 and self.global_step > 0:
                    metrics = self.evaluate(dataset=self.val_dataset, split="val", encode_batch_size=encode_batch_size)
                    self.save_best_checkpoint(metrics)
                    self.policy.train()
                    
        
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
            encode_batch_size=encode_batch_size
        )

        print(f"Final test metrics: {test_metrics}")

    # ------------------------------------------------------------------
    @torch.no_grad()
    def evaluate(
        self,
        dataset: SchemaLinkingDataset | None = None,
        split: str = "val",
        encode_batch_size: int = 64
    ) -> dict:
        self.policy.eval()

        dataset = dataset or self.val_dataset

        total_loss = 0.0
        total_reward = 0.0
        n_batches_processed = 0
        n_examples_processed = 0

        print(f"[{split}] dataset size: {len(dataset)}")

        eval_batch_size = getattr(self.config.training, "eval_batch_size", 8)

        total_batches = math.ceil(len(dataset) / eval_batch_size)
        for batch in tqdm(
            self._iter_batches(dataset, eval_batch_size),
            total=total_batches,
            desc="Evaluating ({split})",
        ):
            loss = compute_db_loss(self.policy, batch, encode_batch_size=encode_batch_size)
            total_loss += loss.item()
            n_batches_processed += 1

            for traj in batch:
                schema = SCHEMAS[traj.example["schema"]]
                terminal_state = self.policy.rollout(traj.query, schema, encode_batch_size=encode_batch_size, greedy=False)
                
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
                n_examples_processed += 1

        metrics = {
            f"{split}_loss": total_loss / max(n_batches_processed, 1),
            f"{split}_reward": total_reward / max(n_examples_processed, 1),
        }

        print(
            f"[{split}] step {self.global_step} "
            f"loss={metrics[f'{split}_loss']:.4f} "
            f"reward={metrics[f'{split}_reward']:.4f}"
        )

        return metrics

    # ------------------------------------------------------------------
    def _checkpoint_dict(self, extra: dict | None = None) -> dict:
        d = {
            "model": self.policy.state_dict(),
            "optimizer": self.optimizer.state_dict(),
            "step": self.global_step,
        }
        if extra:
            d.update(extra)
        return d
    
    def save_checkpoint(self, tag: str = None) -> str:
        cfg = self.config.training
        os.makedirs(cfg.output_dir, exist_ok=True)

        name = tag or f"checkpoint_step{self.global_step}.pt"
        path = os.path.join(cfg.output_dir, name)

        cp_dict = self._checkpoint_dict()
        torch.save(
            cp_dict,
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
            cp_dict = self._checkpoint_dict(extra={"val_reward": metrics["val_reward"], "val_loss": metrics["val_loss"]})
            
            torch.save(
                cp_dict,
                path,
            )
            print(
                f"[checkpoint] new best val_reward={metrics['val_reward']:.4f}, saved to {path}"
            )


if __name__ == "__main__":
    trainer = Trainer(DEFAULT_CONFIG)
    trainer.train()
