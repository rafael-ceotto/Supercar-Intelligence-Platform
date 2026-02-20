from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Supercar Intelligence Platform (MVP)")


class AskRequest(BaseModel):
    question: str


@app.get("/")
def read_root():
    return {"status": "ok", "app": "Supercar Intelligence Platform"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/ask")
def ask(req: AskRequest):
    # Mock response for MVP — replace with RAG/LLM logic later
    return {
        "question": req.question,
        "answer": "Mock answer: pipeline not yet implemented. Replace with RAG+LLM integration."
    }
