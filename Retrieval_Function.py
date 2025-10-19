import pickle
import numpy as np
from sentence_transformers import SentenceTransformer

# Load precomputed embeddings
with open("embeddings.pkl", "rb") as f:
    data = pickle.load(f)

chunks = data["chunks"]
embeddings = data["embeddings"]

# Load lightweight model (optimized for CPU on Render)
def get_model():
    # Very small and fast model (~200MB)
    return SentenceTransformer("sentence-transformers/paraphrase-MiniLM-L3-v2", device="cpu")

model = get_model()

def retrieve_answer(query: str):
    """
    Returns the most relevant chunk and source for any query
    """
    # Embed the query
    query_emb = model.encode([query])[0]

    # Compute cosine similarity
    sims = np.dot(embeddings, query_emb) / (
        np.linalg.norm(embeddings, axis=1) * np.linalg.norm(query_emb)
    )

    # Pick the most relevant chunk
    idx = np.argmax(sims)
    answer = chunks[idx]

    return (answer, "TypeScript Book")
