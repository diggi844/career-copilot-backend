from services.pdf_service import extract_resume_text
from services.ats_service import analyze_resume
from services.role_service import recommend_roles

def process_resume(file_path):

    resume_text = extract_resume_text(
        file_path
    )

    ats_result = analyze_resume(
        resume_text
    )

    role_result = recommend_roles(
        resume_text
    )

    return {
        "resume_text": resume_text,
        "ats_analysis": ats_result,
        "role_recommendations": role_result
    }