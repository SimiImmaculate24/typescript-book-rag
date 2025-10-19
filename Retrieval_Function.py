import torch
torch.set_num_threads(1)
torch.set_num_interop_threads(1)
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer

# Load precomputed embeddings
with open("embeddings.pkl", "rb") as f:
    data = pickle.load(f)

chunks = data["chunks"]
embeddings = data["embeddings"]

# Load lightweight model
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2", device="cpu")

def retrieve_answer(query: str):
    """
    Returns the most relevant chunk and source for any query
    """
    # Embed the query
    query_emb = model.encode([query])[0]

    # Compute cosine similarity
    sims = np.dot(embeddings, query_emb) / (np.linalg.norm(embeddings, axis=1) * np.linalg.norm(query_emb))

    # Return the most relevant chunk
    idx = np.argmax(sims)
    answer = chunks[idx]

    return (answer, "TypeScript Book")