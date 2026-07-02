from dataclasses import dataclass
from typing import Dict, Set, Tuple, List


@dataclass
class SchemaGraph:

    nodes: Set[str]
    relations: Set[str]
    node_props: Dict[str, Set[str]]
    rel_props: Dict[str, Set[str]]
    edges: Set[Tuple[str, str, str]]

    def neighbors(self, node: str) -> List[Tuple[str, str]]:
        result = []
        for src, rel, dst in self.edges:
            if src == node:
                result.append((dst, rel))
        return result

    def relations_between(self, node_a: str, node_b: str) -> List[Tuple[str, str, str]]:

        result = []
        for edge in self.edges:
            src, rel, dst = edge
            if (src == node_a and dst == node_b) or (src == node_b and dst == node_a):
                result.append(edge)
        return result

    def is_valid_edge(self, src: str, rel: str, dst: str) -> bool:
        return (src, rel, dst) in self.edges or (dst, rel, src) in self.edges

    def all_node_properties(self, node: str) -> Set[str]:
        return self.node_props.get(node, set())

    def all_rel_properties(self, rel: str) -> Set[str]:
        return self.rel_props.get(rel, set())

    def describe(self) -> str:

        lines = ["Graph Schema:"]
        lines.append(f"  Nodes: {sorted(self.nodes)}")
        lines.append("  Node Properties:")
        for n, props in sorted(self.node_props.items()):
            lines.append(f"    {n}: {sorted(props)}")
        lines.append("  Relations (src -[rel]-> dst):")
        for src, rel, dst in sorted(self.edges):
            rel_p = sorted(self.rel_props.get(rel, set()))
            lines.append(f"    ({src})-[{rel}]->({dst})  props: {rel_p}")
        return "\n".join(lines)


def schema_from_dict(d: dict) -> SchemaGraph:

    nodes = set(d["nodes"])
    edges = {tuple(e) for e in d["edges"]}
    relations = {e[1] for e in edges}
    node_props = {k: set(v) for k, v in d.get("node_props", {}).items()}
    rel_props = {k: set(v) for k, v in d.get("rel_props", {}).items()}

    return SchemaGraph(
        nodes=nodes,
        relations=relations,
        node_props=node_props,
        rel_props=rel_props,
        edges=edges,
    )
