import json
from datasets import load_dataset

from schemaflow.data.cypher_parser.schema_extractor import extract_schema

ds = load_dataset("megagonlabs/cypherbench")

def convert(example):
    # print("=" * 80)
    # print(example["gold_cypher"])
    return {
        "query": example["nl_question"],
        "schema": example["graph"],
        "gold_cypher": example["gold_cypher"],
        "gold": extract_schema(example["gold_cypher"]),
    }

converted = {}

for split in ds.keys():
    converted[split] = [convert(ex) for ex in ds[split]]
    # converted[split] = [convert(ex) for ex in ds[split].select(range(50))]


for split, data in converted.items():
    output_file = f"cb_{split}.json"

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False, default=list)

    print(f"Saved {len(data)} examples to {output_file}")

print("Done!")