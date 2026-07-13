from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, Tuple, FrozenSet
import torch

from schemaflow.schema.state import SchemaState
from schemaflow.schema.graph import SchemaGraph

@dataclass
class RewardConfig:
    min_reward: float = 1e-3

class SchemaLinkingReward:
    def __init__(self, config: RewardConfig, device: torch.device):
        self.config = config
        self.device = device

    def __call__(
        self,
        state:           SchemaState,
        schema:          SchemaGraph,
        gold_nodes:      Optional[FrozenSet[str]] = None,
        gold_node_props: Optional[FrozenSet[str]] = None,
        gold_rels:       Optional[FrozenSet[Tuple[str, str, str]]] = None,
        gold_rel_props:  Optional[FrozenSet[str]] = None,
    ) -> float:
        assert state.is_terminal, "Reward only defined for terminal states"
        assert gold_nodes is not None and gold_rels is not None, \
            "gold_nodes and gold_rels are required for F1 reward"

        gold_node_props = gold_node_props or frozenset()
        gold_rel_props  = gold_rel_props or frozenset()

        raw = self._f1(
            state,
            gold_nodes=gold_nodes,
            gold_node_props=gold_node_props,
            gold_rels=gold_rels,
            gold_rel_props=gold_rel_props,
        )

        return max(self.config.min_reward, raw)


    @staticmethod
    def _pool(nodes, node_props, rels, rel_props) -> FrozenSet:
        pooled = set()
        pooled.update(("node", x) for x in nodes)
        pooled.update(("node_prop", x) for x in node_props)
        pooled.update(("rel", x) for x in rels)
        pooled.update(("rel_prop", x) for x in rel_props)
        return frozenset(pooled)

    def _f1(
        self,
        state:           SchemaState,
        gold_nodes:      FrozenSet[str],
        gold_node_props: FrozenSet[str],
        gold_rels:       FrozenSet[Tuple[str, str, str]],
        gold_rel_props:  FrozenSet[str],
    ) -> float:
        pred = self._pool(
            state.selected_nodes,
            state.selected_node_props,
            state.selected_relations,
            state.selected_rel_props,
        )
        gold = self._pool(gold_nodes, gold_node_props, gold_rels, gold_rel_props)

        if not pred and not gold:
            return 1.0
        if not pred or not gold:
            return 0.0

        tp = len(pred & gold)
        precision = tp / len(pred)
        recall = tp / len(gold)

        if precision + recall == 0:
            return 0.0

        return 2 * precision * recall / (precision + recall)