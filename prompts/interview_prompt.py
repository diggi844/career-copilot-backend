INTERVIEW_PROMPT = """
You are an expert technical interviewer.

Analyze the resume and identify the most suitable role.

Generate exactly 10 interview questions.

Question Distribution:

- 5 MCQ Questions
- 5 Descriptive Questions

MCQ Format:

MCQ|Question|Option A|Option B|Option C|Option D|Correct Option

Example:

MCQ|What is Snowflake Clustering?|Compression|Data Pruning|Backup|Security|B

Descriptive Format:

TEXT|Explain a Snowflake optimization project you worked on.

Rules:

- Questions must be based on the resume.
- Questions should match the candidate's role.
- Mix SQL, Python, Data Engineering, Analytics and Behavioral topics.
- Start easy and increase difficulty.

Return only questions.

Resume:

{resume}
"""