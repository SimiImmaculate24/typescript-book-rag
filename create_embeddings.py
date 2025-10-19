from sentence_transformers import SentenceTransformer
import pickle
import re

# Load the book text
with open("typescript_book.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Split into chunks (by paragraph)
chunks = re.split(r'\n\n+', text)

# Use a lightweight embedding model
model = SentenceTransformer("paraphrase-MiniLM-L3-v2")

# Compute embeddings
embeddings = model.encode(chunks)

# Save embeddings and chunks
with open("embeddings.pkl", "wb") as f:
    pickle.dump({"chunks": chunks, "embeddings": embeddings}, f)

print("Embeddings created and saved to embeddings.pkl")