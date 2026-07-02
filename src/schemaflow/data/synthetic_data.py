from schemaflow.data.dataset import SchemaLinkingDataset

SYNTHETIC_DATA = [
    {
        "query": "Which habitats do mammals inhabit?",

        "schema": "cb_biology",

        "gold_nodes": {
            "Taxon",
            "Habitat",
        },

        "gold_node_props": {
            ("Taxon", "name"),
            ("Habitat", "name"),
        },

        "gold_rels": {
            ("Taxon", "inhabits", "Habitat"),
        },

        "gold_rel_props": set(),
    },

    {
        "query": "What is the conservation status of the tiger?",

        "schema": "cb_biology",

        "gold_nodes": {
            "Taxon",
            "ConservationStatus",
        },

        "gold_node_props": {
            ("Taxon", "name"),
            ("ConservationStatus", "name"),
        },

        "gold_rels": {
            ("Taxon", "hasConversationStatus", "ConservationStatus"),
        },

        "gold_rel_props": set(),
    },

    {
        "query": "What taxonomic rank does Panthera leo belong to?",

        "schema": "cb_biology",

        "gold_nodes": {
            "Taxon",
            "TaxonRank",
        },

        "gold_node_props": {
            ("Taxon", "name"),
            ("TaxonRank", "name"),
        },

        "gold_rels": {
            ("Taxon", "hasRank", "TaxonRank"),
        },

        "gold_rel_props": set(),
    },

    {
        "query": "Which taxon is the parent of Panthera leo?",

        "schema": "cb_biology",

        "gold_nodes": {
            "Taxon",
        },

        "gold_node_props": {
            ("Taxon", "name"),
        },

        "gold_rels": {
            ("Taxon", "hasParent", "Taxon"),
        },

        "gold_rel_props": set(),
    },

    {
        "query": "What does the lion feed on?",

        "schema": "cb_biology",

        "gold_nodes": {
            "Taxon",
        },

        "gold_node_props": {
            ("Taxon", "name"),
        },

        "gold_rels": {
            ("Taxon", "feedsOn", "Taxon"),
        },

        "gold_rel_props": set(),
    },

    {
        "query": "Which habitats are occupied by endangered species?",

        "schema": "cb_biology",

        "gold_nodes": {
            "Taxon",
            "Habitat",
            "ConservationStatus",
        },

        "gold_node_props": {
            ("Taxon", "name"),
            ("Habitat", "name"),
            ("ConservationStatus", "name"),
        },

        "gold_rels": {
            ("Taxon", "inhabits", "Habitat"),
            ("Taxon", "hasConversationStatus", "ConservationStatus"),
        },

        "gold_rel_props": set(),
    },

    {
        "query": "Show the habitats of carnivorous mammals.",

        "schema": "cb_biology",

        "gold_nodes": {
            "Taxon",
            "Habitat",
        },

        "gold_node_props": {
            ("Taxon", "name"),
            ("Habitat", "name"),
        },

        "gold_rels": {
            ("Taxon", "feedsOn", "Taxon"),
            ("Taxon", "inhabits", "Habitat"),
        },

        "gold_rel_props": set(),
    },

    {
        "query": "List the taxonomic rank and conservation status of lions.",

        "schema": "cb_biology",

        "gold_nodes": {
            "Taxon",
            "TaxonRank",
            "ConservationStatus",
        },

        "gold_node_props": {
            ("Taxon", "name"),
            ("TaxonRank", "name"),
            ("ConservationStatus", "name"),
        },

        "gold_rels": {
            ("Taxon", "hasRank", "TaxonRank"),
            ("Taxon", "hasConversationStatus", "ConservationStatus"),
        },

        "gold_rel_props": set(),
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