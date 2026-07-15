from dataclasses import dataclass
from typing import Dict, Set, Tuple, List


@dataclass
class SchemaGraph:

    nodes: Set[str]
    relations: Set[str]
    node_props: Dict[str, Dict[str, str]]
    rel_props: Dict[str, Dict[str, str]]
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

    def all_node_properties(self, node: str) -> Dict[str, str]:
        return self.node_props.get(node, {})

    def all_rel_properties(self, rel: str) -> Dict[str, str]:
        return self.rel_props.get(rel, {})
    
    def describe(self) -> str:
        lines = []

        lines.append("Node Properties:")
        for label in sorted(self.nodes):
            props = self.node_props.get(label, {})
            prop_str = ", ".join(
                f"{k}: {v}" for k, v in sorted(props.items())
            )
            lines.append(f"  {label} {{ {prop_str} }}")

        lines.append("")
        lines.append("Relationship properties:")
        seen = set()
        for src, rel, dst in sorted(self.edges):
            if (src, rel, dst) in seen:
                continue
            seen.add((src, rel, dst))

            props = self.rel_props.get(rel, {})
            prop_str = ""
            if props:
                prop_str = " { " + ", ".join(
                    f"{k}: {v}" for k, v in sorted(props.items())
                ) + " }"

            lines.append(f"  (:{src})-[:{rel}{prop_str}]->(:{dst})")

        return "\n".join(lines)


def schema_from_dict(d: dict) -> SchemaGraph:
    nodes = {entity["label"] for entity in d["entities"]}

    node_props = {}
    for entity in d["entities"]:
        props = {"name": "str"}  # default property
        props.update(entity.get("properties", {}))
        node_props[entity["label"]] = props

    relations = {rel["label"] for rel in d["relations"]}

    rel_props = {}
    for rel in d["relations"]:
        label = rel["label"]
        rel_props.setdefault(label, {}).update(rel.get("properties", {}))

    edges = {
        (rel["subj_label"], rel["label"], rel["obj_label"])
        for rel in d["relations"]
    }

    return SchemaGraph(
        nodes=nodes,
        relations=relations,
        node_props=node_props,
        rel_props=rel_props,
        edges=edges,
    )