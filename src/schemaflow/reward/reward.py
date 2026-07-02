from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, Tuple, FrozenSet
import torch

from src.schemaflow.schema.state import SchemaState
from src.schemaflow.schema.graph import SchemaGraph


# ──────────────────────────────────────────────────────────────────────
# Config
# ──────────────────────────────────────────────────────────────────────

@dataclass
class RewardConfig:
    min_reward: float = 1e-3  # floor to avoid log(0) in DB loss
    beta:       float = 2.0   # F-beta: >1 weights recall over precision
    weights:    Tuple[float, float, float, float] = (0.25, 0.25, 0.25, 0.25)
    # (w_nodes, w_node_props, w_relations, w_rel_props) — should sum to 1.0


# ──────────────────────────────────────────────────────────────────────
# Reward
# ──────────────────────────────────────────────────────────────────────

class SchemaLinkingReward:
    """
    Computes R(s_terminal) ∈ (0, 1].

    Parameters
    ----------
    config  : RewardConfig
    device  : torch device
    """

    def __init__(self, config: RewardConfig, device: torch.device):
        self.config = config
        self.device = device

    # ------------------------------------------------------------------
    # Main entry point
    # ------------------------------------------------------------------

    def __call__(
        self,
        state:           SchemaState,
        schema:          SchemaGraph,
        gold_nodes:      Optional[FrozenSet[str]] = None,
        gold_node_props: Optional[FrozenSet[str]] = None,
        gold_rels:       Optional[FrozenSet[Tuple[str, str, str]]] = None,
        gold_rel_props:  Optional[FrozenSet[str]] = None,
    ) -> float:
        """
        Returns a scalar reward in (0, 1].

        gold_* args are required — F-beta reward is currently the only
        scoring component, computed against these four gold sets.
        """
        assert state.is_terminal, "Reward only defined for terminal states"
        assert gold_nodes is not None and gold_rels is not None, \
            "gold_nodes and gold_rels are required for F-beta reward"

        gold_node_props = gold_node_props or frozenset()
        gold_rel_props  = gold_rel_props or frozenset()

        raw = self._fbeta(
            state,
            gold_nodes=gold_nodes,
            gold_node_props=gold_node_props,
            gold_rels=gold_rels,
            gold_rel_props=gold_rel_props,
        )

        return max(self.config.min_reward, raw)
    
    
    # ------------------------------------------------------------------
    # F-beta against gold schema
    # ------------------------------------------------------------------

    def _fbeta(
        self,
        state:           SchemaState,
        gold_nodes:      FrozenSet[str],
        gold_node_props: FrozenSet[str],
        gold_rels:       FrozenSet[Tuple[str, str, str]],
        gold_rel_props:  FrozenSet[str],
    ) -> float:
        """
        Weighted F-beta score over selected nodes, node_props, relations,
        and rel_props vs gold. beta > 1 weights recall more than precision,
        penalizing missed schema elements more heavily than extra ones.
        """

        def fbeta_set(pred: FrozenSet, gold: FrozenSet) -> float:
            if not pred and not gold:
                return 1.0
            if not pred or not gold:
                return 0.0

            tp = len(pred & gold)
            precision = tp / len(pred)
            recall    = tp / len(gold)

            if precision + recall == 0:
                return 0.0

            beta_sq = self.config.beta ** 2
            return (1 + beta_sq) * precision * recall / (beta_sq * precision + recall)

        scores = (
            fbeta_set(state.selected_nodes,      gold_nodes),
            fbeta_set(state.selected_node_props, gold_node_props),
            fbeta_set(state.selected_relations,  gold_rels),
            fbeta_set(state.selected_rel_props,  gold_rel_props),
        )

        return sum(w * s for w, s in zip(self.config.weights, scores))
