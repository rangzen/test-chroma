import os
from pprint import pprint

import chromadb

source_relative_path = "~/Documents/second-brain"
source_path = os.path.expanduser(source_relative_path)

chroma_client = chromadb.PersistentClient()

collection = chroma_client.get_or_create_collection(name="test-second-brain")

results = collection.query(
    query_texts=["how to deal with tasks?"],
    n_results=3
)

pprint(results)