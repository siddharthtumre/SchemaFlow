from dataclasses import dataclass
from typing import List
import torch
from torch.utils.data import Dataset

from src.schemaflow.data.utils import enumerate_valid_trajectories
from src.schemaflow.data.schemas import SCHEMAS
from src.schemaflow.schema.state import SchemaState, Action, apply_action, num_parents


@dataclass
class Step:
    state: SchemaState
    action: Action
    next_state: SchemaState
    log_p_b: float


@dataclass
class Trajectory:
    query: str
    example: dict
    steps: List[Step]


class SchemaLinkingDataset(Dataset):

    def __init__(self, ds, max_trajectories: int = 5):
        self.data: List[Trajectory] = []

        for example in ds:
            schema_name = example["schema"]
            schema = SCHEMAS[schema_name]
            trajs = enumerate_valid_trajectories(
                example, max_trajectories=max_trajectories
            )

            for traj in trajs:
                steps: List[Step] = []
                for (state, action) in traj:
                    next_state = apply_action(state, action, schema)
                    k = num_parents(next_state, schema, schema_name)

                    steps.append(Step(
                        state=state,
                        action=action,
                        next_state=next_state,
                        log_p_b=-torch.log(torch.tensor(float(k))).item(),
                    ))

                self.data.append(Trajectory(
                    query=example["query"],
                    example=example,
                    steps=steps,
                ))

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx) -> Trajectory:
        return self.data[idx]