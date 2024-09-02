import os

import chromadb

source_relative_path = "~/Documents/second-brain"
source_path = os.path.expanduser(source_relative_path)

chroma_client = chromadb.PersistentClient()

collection = chroma_client.get_or_create_collection(name="test-second-brain")

# Parse all markdown files in the directory and subdirectories
for root, dirs, files in os.walk(source_path):
    for file in files:
        if file.endswith(".md"):
            file_path = os.path.join(root, file)
            with open(file_path, "r") as f:
                content = f.read()
                print(f"File: {file_path}")
                #print(f"Content: {content}")
                collection.upsert(
                    documents=[content],
                    metadatas=[{"file_path": file_path}],
                    ids=[file_path]
                )
