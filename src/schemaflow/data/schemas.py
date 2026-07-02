from schemaflow.schema.graph import schema_from_dict

BIOLOGY_SCHEMA = schema_from_dict({
    "nodes": [
        "Taxon",
        "ConservationStatus",
        "Habitat",
        "TaxonRank",
    ],
    "edges": [
        ("Taxon", "inhabits", "Habitat"),
        ("Taxon", "hasConversationStatus", "ConservationStatus"),
        ("Taxon", "hasRank", "TaxonRank"),
        ("Taxon", "hasParent", "Taxon"),
        ("Taxon", "feedsOn", "Taxon"),
    ],
    "node_props": {
        "Taxon": ["taxon_name", "name", "longest_lifespan_years", "diel_cycle", "avg_gestation_period_days"],
        "ConservationStatus": ["name"],
        "TaxonRank": ["name"],
        "Habitat": ["name"],
    },
    "rel_props": {
    },
})

SCHEMAS = {
    "cb_biology": BIOLOGY_SCHEMA,
}