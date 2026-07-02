from __future__ import annotations

from dataclasses import dataclass
from typing import List

import torch
import torch.nn as nn
import torch.nn.functional as F
from transformers import AutoModel, AutoTokenizer, BitsAndBytesConfig
from peft import LoraConfig as PeftLoraConfig, get_peft_model, TaskType
from peft import prepare_model_for_kbit_training

from src.schemaflow.policy.utils import serialize_state, serialize_action

from src.schemaflow.schema.state import (
    SchemaState,
    Action,
    apply_action,
    valid_actions,
)
from src.schemaflow.schema.graph import SchemaGraph
from src.schemaflow.config import ModelConfig, LoRAConfig, GFlowNetConfig

class LLM(nn.Module):
    def __init__(self, model_config: ModelConfig, lora_config: LoRAConfig, device: torch.device):
        super().__init__()
        self.device = device

        quant_config = None
        if model_config.load_in_4bit:
            quant_config = BitsAndBytesConfig(
                load_in_4bit=True,
                bnb_4bit_compute_dtype=getattr(torch, model_config.bnb_4bit_compute_dtype),
                bnb_4bit_use_double_quant=True,
                bnb_4bit_quant_type="nf4",
            )

        base_model = AutoModel.from_pretrained(
            model_config.model_name,
            trust_remote_code=True,
            device_map="auto",
            quantization_config=quant_config,
        )
        
        if model_config.load_in_4bit:
            base_model = prepare_model_for_kbit_training(base_model)

        peft_config = PeftLoraConfig(
            task_type=TaskType.CAUSAL_LM,
            r=lora_config.r,
            lora_alpha=lora_config.lora_alpha,
            lora_dropout=lora_config.lora_dropout,
            target_modules=lora_config.target_modules,
            bias="none",
        )

        self.model = get_peft_model(base_model, peft_config)
        self.model.gradient_checkpointing_enable()
        self.tokenizer = AutoTokenizer.from_pretrained(model_config.model_name)
        self.tokenizer.padding_side = "right"
        if self.tokenizer.pad_token is None:
            self.tokenizer.pad_token = self.tokenizer.eos_token

        self.hidden_size = self.model.config.hidden_size

    def encode(self, texts: List[str]) -> torch.Tensor:
        print("Before forward:", torch.cuda.memory_allocated() / 1024**3)
        enc = self.tokenizer(
            texts,
            return_tensors="pt",
            padding=True,
            truncation=True,
            max_length=512,
        ).to(self.device)

        out = self.model(
            **enc,
            return_dict=True,
            use_cache=False,
        )
        last_hidden = out.last_hidden_state
        
        print("After forward:", torch.cuda.memory_allocated() / 1024**3)

        seq_lens = enc["attention_mask"].sum(dim=1) - 1
        batch_idx = torch.arange(last_hidden.size(0), device=last_hidden.device)
        pooled = last_hidden[batch_idx, seq_lens]
        
        return pooled


class PolicyHead(nn.Module):
    def __init__(self, hidden_size: int):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(hidden_size, hidden_size // 2),
            nn.GELU(),
            nn.Linear(hidden_size // 2, 1),
        )

    def forward(self, pooled: torch.Tensor) -> torch.Tensor:
        return self.net(pooled).squeeze(-1)


class FlowHead(nn.Module):
    def __init__(self, hidden_size: int):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(hidden_size, hidden_size // 2),
            nn.GELU(),
            nn.Linear(hidden_size // 2, 1),
        )

    def forward(self, pooled: torch.Tensor) -> torch.Tensor:
        return self.net(pooled).squeeze(-1)


@dataclass
class PolicyOutput:
    actions:      List[Action]
    log_probs:    torch.Tensor
    log_flow:     torch.Tensor


class SchemaFlowPolicy(nn.Module):

    def __init__(
        self,
        model_config: ModelConfig,
        lora_config: LoRAConfig,
        gfn_config:  GFlowNetConfig,
        device:      torch.device,
    ):
        super().__init__()
        self.device = device
        self.gfn_config = gfn_config

        self.llm = LLM(model_config, lora_config, device)
        self.policy_head = PolicyHead(self.llm.hidden_size).to(device)
        self.flow_head = FlowHead(self.llm.hidden_size).to(device)

    # ------------------------------------------------------------------
    def forward(
        self,
        state:    SchemaState,
        schema:   SchemaGraph,
        query: str,
    ) -> PolicyOutput:
        
        actions = valid_actions(state, schema)

        state_text = serialize_state(state, query)
        
        print("=" * 60)
        print("Num actions:", len(actions))
        print("State chars:", len(state_text))
        print("State tokens:", len(self.llm.tokenizer(state_text)["input_ids"]))

        flow_pooled = self.llm.encode([state_text])
        log_flow = self.flow_head(flow_pooled).squeeze(0)
        
        if not actions:
            return PolicyOutput(
                actions=[],
                log_probs=torch.empty(0, device=self.device),
                log_flow=log_flow,
            )

        action_texts = [state_text + serialize_action(a) for a in actions]
        print("Action batch shape:", len(action_texts))
        
        chunk_size = 8
        pooled = []

        for i in range(0, len(action_texts), chunk_size):
            pooled.append(self.llm.encode(action_texts[i:i + chunk_size]))

        action_pooled = torch.cat(pooled, dim=0)
        
        logits = self.policy_head(action_pooled)

        log_probs = F.log_softmax(logits / self.gfn_config.temperature, dim=-1)

        return PolicyOutput(actions=actions, log_probs=log_probs, log_flow=log_flow)

    # ------------------------------------------------------------------
    
    @torch.no_grad()
    def rollout(
        self,
        query: str,
        schema,
        greedy: bool = True,
        max_steps: int = 20,
    ) -> SchemaState:
        state = SchemaState.initial(query)

        for _ in range(max_steps):
            if state.is_terminal:
                break
            out = self(state, schema, query)

            if not out.actions:
                break

            if greedy:
                idx = torch.argmax(out.log_probs).item()
            else:
                probs = out.log_probs.exp()
                idx = torch.multinomial(probs, num_samples=1).item()
            action = out.actions[idx]
            state = apply_action(state, action, schema)

        return state

    # ------------------------------------------------------------------
    def trainable_parameters(self):
        lora_params = [p for p in self.llm.model.parameters() if p.requires_grad]
        head_params = list(self.policy_head.parameters()) + list(self.flow_head.parameters())
        return lora_params + head_params