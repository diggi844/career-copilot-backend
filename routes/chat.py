from fastapi import APIRouter
from pydantic import BaseModel

from agent import ask_llm
from models.chat_store import resume_sessions
from prompts.chat_prompt import CHAT_PROMPT

router = APIRouter()


class ChatRequest(BaseModel):
    session_id: str
    message: str


@router.post("/")
async def chat(request: ChatRequest):

    session = resume_sessions.get(
        request.session_id
    )

    if not session:
        return {
            "response": "Session not found."
        }

    prompt = CHAT_PROMPT.format(
        resume=session["resume_text"],
        ats=session["ats_analysis"],
        roles=session["role_recommendations"],
        history=session["chat_history"],
        question=request.message
    )

    response = ask_llm(prompt)

    session["chat_history"].append(
        {
            "role": "user",
            "content": request.message
        }
    )

    session["chat_history"].append(
        {
            "role": "assistant",
            "content": response
        }
    )

    return {
        "response": response
    }