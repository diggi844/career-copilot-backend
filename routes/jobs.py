from fastapi import APIRouter
from pydantic import BaseModel

from services.job_service import search_jobs
from models.chat_store import resume_sessions

router = APIRouter()


class JobRequest(BaseModel):
    session_id: str
    country: str = ""
    city: str = ""
    work_mode: str = ""
    days: int = 7


@router.post("/")
async def get_jobs(request: JobRequest):

    session = resume_sessions.get(
        request.session_id
    )

    if not session:
        return {
            "jobs": []
        }

    roles = session.get(
        "role_recommendations",
        {}
    )

    role_list = roles.get(
        "roles",
        []
    )

    if not role_list:

        return {
            "error": "No role recommendations found",
            "jobs": []
        }

    best_role = max(
        role_list,
        key=lambda x: x.get(
            "match_percentage",
            0
        )
    )

    role = best_role.get(
        "role"
    )

    job_result = search_jobs(
        role=role,
        country=request.country,
        city=request.city,
        work_mode=request.work_mode,
        days=request.days
    )

    return {
        "role_used": role,
        "query_used": job_result.get(
            "query_used"
        ),
        "jobs": job_result.get(
            "jobs",
            []
        )
    }
