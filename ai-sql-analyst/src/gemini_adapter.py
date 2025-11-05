import os
from dotenv import load_dotenv
import google.generativeai as genai
from prompt_templates import SQL_PROMPT_TEMPLATE

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

def generate_sql_with_gemini(question: str, schema_info: str) -> str:
    model = genai.GenerativeModel("gemini-2.5-pro")
    prompt = SQL_PROMPT_TEMPLATE.format(question=question, schema=schema_info)
    response = model.generate_content(prompt)
    sql = response.text.strip()

    # Remove markdown like ```sql ... ```
    sql = sql.replace("```sql", "").replace("```", "").strip()
    return sql
