from fastapi import APIRouter
from pydantic import BaseModel

from services.ats_service import analyze_resume
from services.improve_service import improve_resume

router = APIRouter()


class ResumeRequest(BaseModel):
    resume_text: str


@router.post("/analyze")
def analyze(request: ResumeRequest):

    result = analyze_resume(
        request.resume_text
    )

    return {
        "analysis": result
    }

@router.post("/improve")
def improve(request: ResumeRequest):

    result = improve_resume(
        request.resume_text
    )

    return {
        "improvement": result
    }