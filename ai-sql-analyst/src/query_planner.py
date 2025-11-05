from db import execute_query
from gemini_adapter import generate_sql_with_gemini
from validators import is_sql_safe

def interpret_and_run(question: str):
    schema_info = """
    Table: bank_marketing
    Columns: age, job, marital, education, default, housing, loan, contact,
             month, day_of_week, duration, campaign, pdays, previous, poutcome,
             emp_var_rate, cons_price_idx, cons_conf_idx, euribor3m, nr_employed, y
    """
    sql_query = generate_sql_with_gemini(question, schema_info)

    # Clean markdown formatting if present
    sql_query = sql_query.replace("```sql", "").replace("```", "").strip()

    if not is_sql_safe(sql_query):
        raise ValueError("Unsafe SQL detected.")
    return execute_query(sql_query)
