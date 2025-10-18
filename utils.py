# utils.py
def split_text(text, chunk_size=500):
    """
    Splits the text into chunks of approximately chunk_size words.
    """
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size):
        chunks.append(" ".join(words[i:i + chunk_size]))
    return chunks