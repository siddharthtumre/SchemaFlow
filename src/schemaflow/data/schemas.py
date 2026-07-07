from pathlib import Path
import json


from schemaflow.schema.graph import SchemaGraph, schema_from_dict

schemas_path = Path("src/schemaflow/data/cypherbench_schemas")

SCHEMAS: dict[str, SchemaGraph] = {}

for schema_file in schemas_path.glob("*.json"):
    with open(schema_file, "r") as f:
        schema_dict = json.load(f)

    SCHEMAS[schema_dict["name"]] = schema_from_dict(schema_dict)
    
    break
print(SCHEMAS)