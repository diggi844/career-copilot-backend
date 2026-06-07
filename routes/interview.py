from fastapi import APIRouter
from pydantic import BaseModel

from services.interview_service import (
    start_interview,
    submit_answer
)

router = APIRouter()


class StartInterviewRequest(BaseModel):
    resume_text: str
    role: str


class AnswerRequest(BaseModel):
    session_id: str
    answer: str


@router.post("/start")
def start(request: StartInterviewRequest):

    return start_interview(
        request.resume_text,
        request.role
    )


@router.post("/answer")
def answer(request: AnswerRequest):

    return submit_answer(
        request.session_id,
        request.answer
    )