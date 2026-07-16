from dataclasses import dataclass, field
from typing import List, Tuple
import json
import torch
import random
from collections import defaultdict

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

random.seed(42)

schema_groups = defaultdict(list)
for example in train_data:
    schema_groups[example["schema"]].append(example)
    
train_split = []
eval_split = []

for examples in schema_groups.values():
    random.shuffle(examples)

    n_val = max(1, round(0.01 * len(examples)))
    eval_split.extend(examples[:n_val])
    train_split.extend(examples[n_val:])

train_data = train_split
eval_data = eval_split
test_data = test_data

@dataclass
class ModelConfig:
    model_name:      str   = "Qwen/Qwen3-4B"
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
    train_data:        List   = field(default_factory=lambda: train_data)
    eval_data:         List   = field(default_factory=lambda: eval_data)
    test_data:         List   = field(default_factory=lambda: test_data)
    output_dir:        str   = "checkpoints_qwen3_4b"
    # Training
    num_epochs:        int   = 2
    shuffle:           bool  = True
    accum_steps:       int   = 2
    train_batch_size:  int   = 8
    eval_batch_size:   int   = 8
    encode_batch_size: int   = 64
    lr:                float = 1e-5
    grad_clip:         float = 1.0
    # Logging
    log_every:         int   = 200
    eval_every:        int   = 1000
    # Seed
    seed:              int   = 42


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
