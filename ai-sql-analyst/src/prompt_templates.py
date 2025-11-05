SQL_PROMPT_TEMPLATE = """
You are an expert data analyst. Convert the user question into a valid DuckDB SQL query.

Schema:
{schema}

Question:
{question}

Return ONLY the SQL query.
"""
