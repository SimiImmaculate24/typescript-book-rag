# create_embeddings.py
from sentence_transformers import SentenceTransformer
import pickle
from utils import split_text

# Load the TypeScript book robustly
with open("typescript_book.txt", "r", encoding="utf-8", errors="ignore") as f:
    text = f.read()

# Split into chunks
chunks = split_text(text, chunk_size=500)

# Load model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Generate embeddings
print("Generating embeddings... this may take a few minutes")
embeddings = model.encode(chunks, show_progress_bar=True)

# Save chunks and embeddings
with open("embeddings.pkl", "wb") as f:
    pickle.dump({"chunks": chunks, "embeddings": embeddings}, f)

print("Saved embeddings.pkl successfully")