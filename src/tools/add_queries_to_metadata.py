import json
import yaml
from pathlib import Path

THIS_FILE = Path(__file__)
THIS_DIR = THIS_FILE.parent
DATASETTE_DIR = THIS_DIR.joinpath("../../datasette/")

# from datasette/utils
class BadMetadataError(Exception):
    pass

def parse_metadata(content):
    # content can be JSON or YAML
    try:
        return json.loads(content)
    except json.JSONDecodeError:
        try:
            return yaml.safe_load(content)
        except yaml.YAMLError:
            raise BadMetadataError("Metadata is not valid JSON or YAML")

with open(DATASETTE_DIR / "metadata.json", "r") as file:
    metadata = parse_metadata(file.read())

with open(DATASETTE_DIR / "queries.yaml", "r") as file:
    queries = parse_metadata(file.read())

metadata['databases']['ripa-2018-db']['queries'] = {}
for query in queries.keys():
    metadata['databases']['ripa-2018-db']['queries'][query] = queries[query]

with open(DATASETTE_DIR / "updated_metadata.json", "w") as file:
    file.write(json.dumps(metadata, indent=4),)