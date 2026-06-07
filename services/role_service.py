import json

from agent import ask_llm
from prompts.role_prompt import ROLE_PROMPT


def recommend_roles(resume_text: str):

    response = ask_llm(
        ROLE_PROMPT.format(
            resume=resume_text
        )
    )

    try:
        return json.loads(response)

    except Exception:

        return {
            "roles": [],
            "raw_response": response
        }