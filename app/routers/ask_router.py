from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class AskRequest(BaseModel):
    question: str


@router.post("/ask")
def ask_endpoint(req: AskRequest):
    return {"question": req.question, "answer": "Mock answer from router"}
