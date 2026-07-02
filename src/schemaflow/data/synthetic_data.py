from schemaflow.data.dataset import SchemaLinkingDataset

SYNTHETIC_DATA = [
    {
        "query": "Which habitats do mammals inhabit?",
        "schema": "cb_biology",
        "gold": {
            "nodes": {
                "Taxon",
                "Habitat",
            },
            "node_props": {
                ("Taxon", "name"),
                ("Habitat", "name"),
            },
            "relations": {
                ("Taxon", "inhabits", "Habitat"),
            },
            "relation_props": set(),
        },
    },
    {
        "query": "What is the conservation status of the tiger?",
        "schema": "cb_biology",
        "gold": {
            "nodes": {
                "Taxon",
                "ConservationStatus",
            },
            "node_props": {
                ("Taxon", "name"),
                ("ConservationStatus", "name"),
            },
            "relations": {
                ("Taxon", "hasConversationStatus", "ConservationStatus"),
            },
            "relation_props": set(),
        },
    },
    {
        "query": "What taxonomic rank does Panthera leo belong to?",
        "schema": "cb_biology",
        "gold": {
            "nodes": {
                "Taxon",
                "TaxonRank",
            },
            "node_props": {
                ("Taxon", "name"),
                ("TaxonRank", "name"),
            },
            "relations": {
                ("Taxon", "hasRank", "TaxonRank"),
            },
            "relation_props": set(),
        },
    },
    {
        "query": "Which taxon is the parent of Panthera leo?",
        "schema": "cb_biology",
        "gold": {
            "nodes": {
                "Taxon",
            },
            "node_props": {
                ("Taxon", "name"),
            },
            "relations": {
                ("Taxon", "hasParent", "Taxon"),
            },
            "relation_props": set(),
        },
    },
    {
        "query": "What does the lion feed on?",
        "schema": "cb_biology",
        "gold": {
            "nodes": {
                "Taxon",
            },
            "node_props": {
                ("Taxon", "name"),
            },
            "relations": {
                ("Taxon", "feedsOn", "Taxon"),
            },
            "relation_props": set(),
        },
    },
    {
        "query": "Which habitats are occupied by endangered species?",
        "schema": "cb_biology",
        "gold": {
            "nodes": {
                "Taxon",
                "Habitat",
                "ConservationStatus",
            },
            "node_props": {
                ("Taxon", "name"),
                ("Habitat", "name"),
                ("ConservationStatus", "name"),
            },
            "relations": {
                ("Taxon", "inhabits", "Habitat"),
                ("Taxon", "hasConversationStatus", "ConservationStatus"),
            },
            "relation_props": set(),
        },
    },
    {
        "query": "Show the habitats of carnivorous mammals.",
        "schema": "cb_biology",
        "gold": {
            "nodes": {
                "Taxon",
                "Habitat",
            },
            "node_props": {
                ("Taxon", "name"),
                ("Habitat", "name"),
            },
            "relations": {
                ("Taxon", "feedsOn", "Taxon"),
                ("Taxon", "inhabits", "Habitat"),
            },
            "relation_props": set(),
        },
    },
    {
        "query": "List the taxonomic rank and conservation status of lions.",
        "schema": "cb_biology",
        "gold": {
            "nodes": {
                "Taxon",
                "TaxonRank",
                "ConservationStatus",
            },
            "node_props": {
                ("Taxon", "name"),
                ("TaxonRank", "name"),
                ("ConservationStatus", "name"),
            },
            "relations": {
                ("Taxon", "hasRank", "TaxonRank"),
                ("Taxon", "hasConversationStatus", "ConservationStatus"),
            },
            "relation_props": set(),
        },
    },
]


# dataset = SchemaLinkingDataset(SYNTHETIC_DATA, max_trajectories=None)
# print(f"Created synthetic dataset with {len(dataset)} trajectories.")

# for i, traj in enumerate(dataset.data[:3]):
#     print(f"\n{'='*60}")
#     print(f"Sample {i + 1}  |  query: {traj.query!r}")
#     print(f"{'='*60}")

#     for j, step in enumerate(traj.steps):
#         print(f"\nStep {j}")
#         print(f"  state      : {step.state}")
#         print(f"  action     : {step.action}")
#         print(f"  next_state : {step.next_state}")
#         print(f"  log_p_b    : {step.log_p_b:.4f}  (P_B = {2.718281828 ** step.log_p_b:.4f})")