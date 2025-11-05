import streamlit as st
from db import execute_query, get_db_metadata
from gemini_adapter import generate_sql_with_gemini
from query_planner import interpret_and_run
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="AI SQL Analyst", page_icon="📊", layout="wide")
st.title("AI SQL Analyst")
st.markdown("Ask questions & get instant SQL + insights powered by Gemini & DuckDB.")

# === SHOW DATABASE INFO ===
db_name, table_info = get_db_metadata()
with st.expander(f"🗄️ Database Info — {db_name}", expanded=False):
    for table, columns in table_info.items():
        st.markdown(f"**Table:** `{table}`")
        st.markdown(", ".join(f"`{col}`" for col in columns))

user_query = st.text_input("💬 Ask a question about the data:")
if st.button("Run Query") and user_query:
    with st.spinner("💡Analyzing..."):
        result = interpret_and_run(user_query)
        st.write("### 📊 Result")
        st.dataframe(result)
