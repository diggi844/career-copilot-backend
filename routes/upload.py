import os
import shutil
import uuid

from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File

from services.resume_orchestrator import process_resume


from models.chat_store import resume_sessions

router = APIRouter()

UPLOAD_DIR = "uploads"

os.makedirs(
    UPLOAD_DIR,
    exist_ok=True
)

@router.post("/resume")
async def upload_resume(
    file: UploadFile = File(...)
):

    file_path = os.path.join(
        UPLOAD_DIR,
        file.filename
    )

    with open(
        file_path,
        "wb"
    ) as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )

    result = process_resume(
    file_path
)

    session_id = str(uuid.uuid4())

    resume_sessions[session_id] = {
        "resume_text": result["resume_text"],
        "ats_analysis": result["ats_analysis"],
        "role_recommendations": result["role_recommendations"],
        "chat_history": []
    }

    result["session_id"] = session_id

    return result