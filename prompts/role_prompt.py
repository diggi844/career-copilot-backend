ROLE_PROMPT = """
Analyze the resume and return ONLY valid JSON.

Format:

{{
  "roles": [
    {{
      "role": "",
      "match_percentage": 0,
      "reason": ""
    }}
  ]
}}

Rules:
- Return exactly 5 roles
- match_percentage should be between 0 and 100
- role should be concise
- reason should be max 1 sentence
- Return ONLY JSON
- No markdown
- No explanations

Resume:

{resume}
"""