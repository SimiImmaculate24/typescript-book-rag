import pickle
from sentence_transformers import SentenceTransformer
import numpy as np

# Load embeddings and chunks
with open("embeddings.pkl", "rb") as f:
    data = pickle.load(f)

chunks = data["chunks"]
embeddings = data["embeddings"]

# Load model
model = SentenceTransformer("all-MiniLM-L6-v2")

def retrieve_answer(query: str):
    # Embed query
    query_emb = model.encode([query])[0]

    # Compute cosine similarity
    sims = np.dot(embeddings, query_emb) / (np.linalg.norm(embeddings, axis=1) * np.linalg.norm(query_emb))

    # Pick the most similar chunk
    idx = np.argmax(sims)
    answer = chunks[idx]

    # You can optionally trim or return the exact line that contains the answer
    return (answer, "TypeScript Book")
