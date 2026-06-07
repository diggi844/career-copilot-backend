EVALUATION_PROMPT = """
Question:
{question}

Candidate Answer:
{answer}

Evaluate the answer.

Return ONLY in the format below:

Technical Accuracy: X/10

Communication: X/10

Business Thinking: X/10

Strengths:
- Point 1
- Point 2

Improvements:
- Point 1
- Point 2

Keep feedback concise.
Maximum 100 words.
"""