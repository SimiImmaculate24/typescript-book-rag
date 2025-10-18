from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from Retrieval_Function import retrieve_answer

app = FastAPI()

# Enable CORS
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
