import json

from agent import ask_llm
from prompts.ats_prompt import ATS_PROMPT


def analyze_resume(resume_text: str):

    response = ask_llm(
        ATS_PROMPT.format(
            resume=resume_text
        )
    )

    try:
        return json.loads(response)

    except Exception:

        return {
            "ats_score": 0,
            "strengths": [],
            "weaknesses": [],
            "missing_keywords": [],
            "improvement_suggestions": [],
            "raw_response": response
        }