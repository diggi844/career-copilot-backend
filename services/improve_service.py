from agent import ask_llm
from prompts.improve_resume_prompt import IMPROVE_RESUME_PROMPT

def improve_resume(resume_text: str):

    return ask_llm(
        IMPROVE_RESUME_PROMPT.format(
            resume=resume_text
        )
    )