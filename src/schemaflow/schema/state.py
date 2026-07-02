from __future__ import annotations
from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Dict, FrozenSet, List, Optional, Set, Tuple
from collections import Counter

from src.schemaflow.data.schemas import SCHEMAS
from src.schemaflow.schema.graph import SchemaGraph
from functools import lru_cache

class ActionType(Enum):
    ADD_NODE = auto()
    ADD_NODE_PROP = auto()
    ADD_RELATION_PROP = auto()
    EOS = auto()


@dataclass(frozen=True)
class Action:
    type: ActionType
    node: Optional[str] = None
    src: Optional[str] = None
    dst: Optional[str] = None
    relation: Optional[str] = None
    prop: Optional[str] = None

    def __str__(self) -> str:
        if self.type == ActionType.ADD_NODE:
            if self.node is not None:
                return f"ADD_NODE({self.node})"
            return f"ADD_NODE({self.src}, {self.relation}, {self.dst})"

        if self.type == ActionType.ADD_NODE_PROP:
            return f"ADD_NODE_PROP({self.node}, {self.prop})"

        if self.type == ActionType.ADD_RELATION_PROP:
            return f"ADD_RELATION_PROP({self.relation}, {self.prop})"
        return "EOS"


@dataclass(frozen=True)
class SchemaState:
    query: str
    selected_nodes: FrozenSet[str] = field(default_factory=frozenset)
    selected_node_props: FrozenSet[Tuple[str, str]] = field(default_factory=frozenset)
    selected_relations: FrozenSet[Tuple[str, str, str]] = field(
        default_factory=frozenset
    )
    selected_rel_props: FrozenSet[Tuple[str, str]] = field(default_factory=frozenset)
    is_terminal: bool = False
    
    @classmethod
    def initial(cls, query: str) -> "SchemaState":
        return cls(
            query=query,
            selected_nodes=frozenset(),
            selected_node_props=frozenset(),
            selected_relations=frozenset(),
            selected_rel_props=frozenset(),
            is_terminal=False,
        )

    def node_props_for(self, node: str) -> Set[str]:
        return {p for (n, p) in self.selected_node_props if n == node}

    def rel_props_for(self, rel: str) -> Set[str]:
        return {p for (r, p) in self.selected_rel_props if r == rel}

    def selected_rel_types(self) -> Set[str]:
        return {rel for (_, rel, _) in self.selected_relations}

    def describe(self) -> str:
        lines = ["Current Selection:"]
        lines.append(f"  Nodes     : {sorted(self.selected_nodes) or '(none)'}")

        np: Dict[str, List[str]] = {}
        for n, p in self.selected_node_props:
            np.setdefault(n, []).append(p)
        lines.append(f"  Node Props: {dict(sorted(np.items())) or '(none)'}")

        lines.append(f"  Relations : {sorted(self.selected_relations) or '(none)'}")

        rp: Dict[str, List[str]] = {}
        for r, p in self.selected_rel_props:
            rp.setdefault(r, []).append(p)
        lines.append(f"  Rel Props : {dict(sorted(rp.items())) or '(none)'}")

        return "\n".join(lines)


def _neighbor_edges(
    selected_nodes: FrozenSet[str],
    schema: SchemaGraph,
) -> Set[Tuple[str, str, str]]:

    neighbors: Set[Tuple[str, str, str]] = set()

    for src, rel, dst in schema.edges:
        if src in selected_nodes and dst not in selected_nodes:
            neighbors.add((src, rel, dst))

    return neighbors


def valid_actions(state: SchemaState, schema: SchemaGraph) -> List[Action]:

    actions: List[Action] = []

    if state.is_terminal:
        return actions

    if not state.selected_nodes:
        for node in sorted(schema.nodes):
            actions.append(Action(ActionType.ADD_NODE, node=node))
        return actions

    # Expand to a new node.
    for src, rel, dst in sorted(_neighbor_edges(state.selected_nodes, schema)):
        actions.append(
            Action(
                ActionType.ADD_NODE,
                src=src,
                relation=rel,
                dst=dst,
            )
        )

    # Add node properties.
    for node in sorted(state.selected_nodes):
        for prop in sorted(schema.all_node_properties(node)):
            if (node, prop) not in state.selected_node_props:
                actions.append(Action(ActionType.ADD_NODE_PROP, node=node, prop=prop))

    # Add relation properties.
    for rel in sorted(state.selected_rel_types()):
        for prop in sorted(schema.all_rel_properties(rel)):
            if (rel, prop) not in state.selected_rel_props:
                actions.append(
                    Action(
                        ActionType.ADD_RELATION_PROP,
                        relation=rel,
                        prop=prop,
                    )
                )

    actions.append(Action(ActionType.EOS))

    return actions


def apply_action(
    state: SchemaState, action: Action, schema: SchemaGraph
) -> SchemaState:

    if action.type == ActionType.ADD_NODE:
        if action.node is not None:
            return SchemaState(
                query=state.query,
                selected_nodes=state.selected_nodes | {action.node},
                selected_node_props=state.selected_node_props,
                selected_relations=state.selected_relations,
                selected_rel_props=state.selected_rel_props,
            )
        elif action.src is not None:
            return SchemaState(
                query=state.query,
                selected_nodes=state.selected_nodes | {action.dst},
                selected_node_props=state.selected_node_props,
                selected_relations=state.selected_relations
                | {(action.src, action.relation, action.dst)},
                selected_rel_props=state.selected_rel_props,
            )
        else:
            raise ValueError("Malformed ADD_NODE action.")

    if action.type == ActionType.ADD_NODE_PROP:
        return SchemaState(
            query=state.query,
            selected_nodes=state.selected_nodes,
            selected_node_props=state.selected_node_props
            | {(action.node, action.prop)},
            selected_relations=state.selected_relations,
            selected_rel_props=state.selected_rel_props,
        )

    if action.type == ActionType.ADD_RELATION_PROP:
        return SchemaState(
            query=state.query,
            selected_nodes=state.selected_nodes,
            selected_node_props=state.selected_node_props,
            selected_relations=state.selected_relations,
            selected_rel_props=state.selected_rel_props
            | {(action.relation, action.prop)},
        )

    if action.type == ActionType.EOS:
        return SchemaState(
            query=state.query,
            selected_nodes=state.selected_nodes,
            selected_node_props=state.selected_node_props,
            selected_relations=state.selected_relations,
            selected_rel_props=state.selected_rel_props,
            is_terminal=True,
        )

    raise ValueError(f"Unknown action type: {action.type}")


def _get_parents_impl(
    state: SchemaState, schema: SchemaGraph
) -> List[Tuple[SchemaState, Action]]:

    parents: List[Tuple[SchemaState, Action]] = []

    # --- EOS: only parent is the non-terminal twin ---
    if state.is_terminal:
        parent = SchemaState(
            query=state.query,
            selected_nodes=state.selected_nodes,
            selected_node_props=state.selected_node_props,
            selected_relations=state.selected_relations,
            selected_rel_props=state.selected_rel_props,
            is_terminal=False,
        )
        return [(parent, Action(ActionType.EOS))]

    # --- s0 has no parents ---
    if not state.selected_nodes:
        return []

    # --- Undo ADD_NODE_PROP ---
    for node, prop in state.selected_node_props:
        parent = SchemaState(
            query=state.query,
            selected_nodes=state.selected_nodes,
            selected_node_props=state.selected_node_props - {(node, prop)},
            selected_relations=state.selected_relations,
            selected_rel_props=state.selected_rel_props,
        )
        parents.append((parent, Action(ActionType.ADD_NODE_PROP, node=node, prop=prop)))

    # --- Undo ADD_RELATION_PROP ---
    for rel, prop in state.selected_rel_props:
        parent = SchemaState(
            query=state.query,
            selected_nodes=state.selected_nodes,
            selected_node_props=state.selected_node_props,
            selected_relations=state.selected_relations,
            selected_rel_props=state.selected_rel_props - {(rel, prop)},
        )
        parents.append(
            (parent, Action(ActionType.ADD_RELATION_PROP, relation=rel, prop=prop))
        )

    # --- Undo ADD_NODE(src, rel, dst) ---
    rel_type_counts = Counter(r for (_, r, _) in state.selected_relations)

    for src, rel, dst in state.selected_relations:
        assert (src, rel, dst) in schema.edges, f"Edge {(src,rel,dst)} not in schema!"
        if state.node_props_for(dst):
            continue  # dst carries props added after it was introduced
        if any(s == dst for (s, _, _) in state.selected_relations):
            continue  # dst was itself used to expand further — can't undo yet
        if rel_type_counts[rel] == 1 and state.rel_props_for(rel):
            continue  # this is the only edge of `rel`, and it has rel-props

        parent = SchemaState(
            query=state.query,
            selected_nodes=state.selected_nodes - {dst},
            selected_node_props=state.selected_node_props,
            selected_relations=state.selected_relations - {(src, rel, dst)},
            selected_rel_props=state.selected_rel_props,
        )
        parents.append(
            (parent, Action(ActionType.ADD_NODE, src=src, relation=rel, dst=dst))
        )

    # --- Undo ADD_NODE(root) ---
    if (
        len(state.selected_nodes) == 1
        and not state.selected_relations
        and not state.selected_node_props
        and not state.selected_rel_props
    ):
        (only_node,) = tuple(state.selected_nodes)
        parent = SchemaState(query=state.query)
        parents.append((parent, Action(ActionType.ADD_NODE, node=only_node)))

    return parents


def get_parents(state: SchemaState, schema: SchemaGraph, _validate: bool = True) -> List[Tuple[SchemaState, Action]]:
    parents = _get_parents_impl(state, schema)
    if _validate:
        for parent, action in parents:
            reconstructed = apply_action(parent, action, schema)
            assert reconstructed == state, (
                f"get_parents produced invalid pair.\n"
                f"  parent={parent}\n  action={action}\n"
                f"  apply_action(parent,action)={reconstructed}\n  expected={state}"
            )
    return parents


@lru_cache(maxsize=None)
def _get_parents_cached(state: SchemaState, schema_name: str) -> tuple:
    schema = SCHEMAS[schema_name]
    return tuple(get_parents(state, schema, _validate=False))


def num_parents(state: SchemaState, schema: SchemaGraph, schema_name: str = None) -> int:
    if not state.selected_nodes and not state.is_terminal:
        return 0  # s0
    if schema_name is not None:
        k = len(_get_parents_cached(state, schema_name))
    else:
        k = len(get_parents(state, schema))
    if k == 0:
        raise ValueError(f"Unexpected zero parents for non-root state: {state}")
    return k


def log_backward_prob(state: SchemaState, schema: SchemaGraph) -> float:
    import math

    k = num_parents(state, schema)
    if k == 0:
        raise ValueError("s0 has no parents — backward prob undefined.")
    return -math.log(k)
