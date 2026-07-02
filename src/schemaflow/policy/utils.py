from src.schemaflow.schema.state import Action, SchemaState


def serialize_state(state: SchemaState, question: str) -> str:
    nodes      = ", ".join(state.selected_nodes)
    node_props = ", ".join(sorted(f"{n}.{p}" for n, p in state.selected_node_props))
    
    relations  = ", ".join(f"({s})-[{r}]->({d})" for s, r, d in state.selected_relations)
    rel_props  = ", ".join(sorted(f"{r}.{p}" for r, p in state.selected_rel_props))

    return (
        f"Question: {question}\n"
        f"Selected nodes: {nodes}\n"
        f"Selected node properties: {node_props}\n"
        f"Selected relations: {relations}\n"
        f"Selected relation properties: {rel_props}\n"
    )


def serialize_action(action: Action) -> str:
    return f"Candidate action: {str(action)}"