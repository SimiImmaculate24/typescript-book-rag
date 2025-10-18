from sentence_transformers import SentenceTransformer
import pickle

# Load book
with open("typescript_book.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Split into chunks
import re
chunks = re.split(r'\n\n+', text)  # split by paragraphs

# Compute embeddings
model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(chunks)

# Save embeddings and chunks
with open("embeddings.pkl", "wb") as f:
    pickle.dump({"chunks": chunks, "embeddings": embeddings}, f)
