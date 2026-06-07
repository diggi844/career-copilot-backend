import uuid

from agent import ask_llm

from prompts.interview_prompt import INTERVIEW_PROMPT
from prompts.evaluation_prompt import EVALUATION_PROMPT

from models.interview_store import interview_sessions


def start_interview(
    resume_text,
    role
):

    questions_text = ask_llm(
        INTERVIEW_PROMPT.format(
            resume=resume_text
        )
    )

    questions = [
        q.strip()
        for q in questions_text.split("\n")
        if q.strip()
    ]

    session_id = str(uuid.uuid4())

    interview_sessions[session_id] = {
        "questions": questions,
        "current_index": 0,
        "scores": []
    }

    return {
        "session_id": session_id,
        "question": questions[0],
        "role": role
    }


def submit_answer(session_id, answer):

    session = interview_sessions[session_id]

    current_index = session["current_index"]

    question = session["questions"][current_index]

    feedback = ask_llm(
        EVALUATION_PROMPT.format(
            question=question,
            answer=answer
        )
    )

    session["scores"].append(feedback)

    session["current_index"] += 1

    if session["current_index"] >= len(session["questions"]):

        final_feedback = ask_llm(
            f"""
            Below are interview evaluations:

            {' '.join(session['scores'])}

            Create a FINAL INTERVIEW REPORT.

            Return ONLY:

            Overall Score: X/10

            Strengths:
            - Point 1
            - Point 2
            - Point 3

            Areas For Improvement:
            - Point 1
            - Point 2
            - Point 3

            Hiring Recommendation:
            Strong Hire / Hire / Borderline / No Hire

            Keep response under 150 words.
            """
        )

        return {
            "completed": True,
            "feedback": final_feedback
        }

    next_question = session["questions"][
        session["current_index"]
    ]

    return {
        "completed": False,
        "feedback": feedback,
        "next_question": next_question
    }