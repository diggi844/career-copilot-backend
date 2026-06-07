from fastapi import APIRouter
from pydantic import BaseModel

from services.role_service import recommend_roles

router = APIRouter()

class RoleRequest(BaseModel):
    resume_text: str

@router.post("/recommend")
def recommend(request: RoleRequest):

    result = recommend_roles(
        request.resume_text
    )

    return {
        "roles": result
    }