from src.schemaflow.schema.state import SchemaState, ActionType, apply_action, valid_actions
from src.schemaflow.data.schemas import SCHEMAS

from copy import deepcopy

def is_action_consistent_with_gold(action, example):
    
    if action.type == ActionType.ADD_NODE:
        if action.node is not None:
            return action.node in example["gold_nodes"]
        elif action.src is not None and action.dst is not None and action.relation is not None:
            return (action.src, action.relation, action.dst) in example["gold_rels"]
    elif action.type == ActionType.ADD_NODE_PROP:
        return (action.node, action.prop) in example["gold_node_props"]
    elif action.type == ActionType.ADD_RELATION_PROP:
        return (action.relation, action.prop) in example["gold_rel_props"]
    elif action.type == ActionType.EOS:
        return True
    else:
        raise ValueError(f"Unknown action type: {action.type}")
    

def is_goal_state(
    state: SchemaState,
    example: dict,
) -> bool:
    
    return (
        state.selected_nodes == example["gold_nodes"]
        and
        state.selected_node_props == example["gold_node_props"]
        and
        state.selected_relations == example["gold_rels"]
        and
        state.selected_rel_props == example["gold_rel_props"]
    )
    

def enumerate_valid_trajectories(
    example,
    max_trajectories: int = 5,
):

    schema = SCHEMAS[example["schema"]]

    trajectories = []

    def dfs(state: SchemaState, trajectory):

        # Stop if enough trajectories have been generated
        if max_trajectories and len(trajectories) >= max_trajectories:
            return

        # Finished trajectory
        if state.is_terminal:
            if is_goal_state(state, example):
                trajectories.append(deepcopy(trajectory))
            return

        actions = valid_actions(state, schema)

        gold_actions = [
            action
            for action in actions
            if is_action_consistent_with_gold(action, example)
        ]

        for action in gold_actions:

            next_state = apply_action(state, action, schema)

            trajectory.append((state, action))

            dfs(next_state, trajectory)

            trajectory.pop()

            if max_trajectories and len(trajectories) >= max_trajectories:
                return

    start_state = SchemaState(query=example["query"])

    dfs(start_state, [])

    return trajectories
