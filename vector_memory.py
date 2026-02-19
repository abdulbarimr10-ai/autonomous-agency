# vector_memory.py

import os
import numpy as np
from pymongo import MongoClient
from langchain_ollama import OllamaEmbeddings
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(os.getenv("MONGO_URI"))
db = client["autonomous_agency"]
vector_collection = db["vector_memory"]

# Embedding model
embeddings = OllamaEmbeddings(
    model="nomic-embed-text",
    base_url="http://localhost:11434"
)

def store_embedding(text, metadata):
    vector = embeddings.embed_query(text)

    document = {
        "embedding": vector,
        "text": text,
        "metadata": metadata
    }

    vector_collection.insert_one(document)
    print("🧠 Stored vector memory")


def retrieve_similar(text, top_k=3):
    query_vector = embeddings.embed_query(text)

    docs = list(vector_collection.find())

    scored = []
    for doc in docs:
        score = cosine_similarity(query_vector, doc["embedding"])
        scored.append((score, doc))

    scored.sort(reverse=True, key=lambda x: x[0])

    return [doc for score, doc in scored[:top_k]]


def cosine_similarity(a, b):
    a = np.array(a)
    b = np.array(b)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
