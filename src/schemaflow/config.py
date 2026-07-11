from dataclasses import dataclass, field
from typing import List, Tuple
import json
import torch

def map_data_types(data):
    for example in data:
        gold = example["gold"]

        gold["nodes"] = set(gold["nodes"])
        gold["node_props"] = {tuple(x) for x in gold["node_props"]}
        gold["relations"] = {tuple(x) for x in gold["relations"]}
        gold["relation_props"] = {tuple(x) for x in gold["relation_props"]}

    return data

train_datapath = "src/schemaflow/data/cb_train.json"
test_datapath = "src/schemaflow/data/cb_test.json"

with open(train_datapath, "r", encoding="utf-8") as f:
    train_data = json.load(f)

with open(test_datapath, "r", encoding="utf-8") as f:
    test_data = json.load(f)
    
train_data = map_data_types(train_data)
test_data = map_data_types(test_data)

split_idx = int(0.9 * len(train_data))

original_train_data = train_data
train_data = original_train_data[0:split_idx]
eval_data = original_train_data[split_idx:]

test_data = test_data

@dataclass
class ModelConfig:
    model_name:      str   = "Qwen/Qwen3-0.6B"
    load_in_4bit:    bool  = False
    bnb_4bit_compute_dtype: str = "bfloat16"

@dataclass
class LoRAConfig:
    r:               int   = 16
    lora_alpha:      int   = 32
    lora_dropout:    float = 0.05
    target_modules:  list  = field(default_factory=lambda: [
        "q_proj", "k_proj", "v_proj", "o_proj"
    ])


@dataclass
class GFlowNetConfig:
    objective:       str   = "tb"
    log_z_init:      float = 0.0
    backward_policy: str   = "uniform"
    temperature:     float = 1.0
    max_steps:       int   = 20


@dataclass
class TrainingConfig:
    # Paths
    train_data:      List   = field(default_factory=lambda: train_data)
    eval_data:       List   = field(default_factory=lambda: eval_data)
    test_data:       List   = field(default_factory=lambda: test_data)
    output_dir:      str   = "checkpoints/"
    # Training
    num_epochs:      int   = 2
    shuffle:         bool  = True
    accum_steps:     int   = 2
    train_batch_size:int   = 16
    eval_batch_size: int   = 16
    lr:              float = 1e-4
    grad_clip:       float = 1.0
    # Logging
    log_every:       int   = 50
    # Seed
    seed:            int   = 42


@dataclass
class RewardConfig:
    min_reward: float = 1e-3
    beta:       float = 2.0
    weights:    Tuple[float, float, float, float] = (0.25, 0.25, 0.25, 0.25)


@dataclass
class Config:
    model:    ModelConfig    = field(default_factory=ModelConfig)
    lora:     LoRAConfig     = field(default_factory=LoRAConfig)
    gfn:      GFlowNetConfig = field(default_factory=GFlowNetConfig)
    training: TrainingConfig = field(default_factory=TrainingConfig)
    reward:   RewardConfig   = field(default_factory=RewardConfig)

    @property
    def device(self) -> torch.device:
        return torch.device("cuda" if torch.cuda.is_available() else "cpu")

    def __post_init__(self):
        print(f"[Config] Device: {self.device}")
        if self.device.type == "cuda":
            import torch
            print(f"[Config] GPU: {torch.cuda.get_device_name(0)}")
            print(f"[Config] VRAM: {torch.cuda.get_device_properties(0).total_memory / 1e9:.1f} GB")


DEFAULT_CONFIG = Config()
