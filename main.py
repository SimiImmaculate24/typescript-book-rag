from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from Retrieval_Function import retrieve_answer
import os

app = FastAPI()

# Enable CORS (for portal testing)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/search")
def search(q: str = Query(..., description="User question")):
    answer, source = retrieve_answer(q)
    return {"answer": answer, "sources": source}

# Render/Local entrypoint
if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
