from loguru import logger

import chromadb

logger.info("initializing the chromadb")
client = chromadb.PersistentClient(path="../content/chroma")
collection = client.get_or_create_collection("test")
