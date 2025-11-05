# AI SQL Agent

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Welcome to my AI SQL Agent repository. This project showcases my skills in building AI-powered applications that can understand natural language and interact with databases.

## Project

This repository contains the following main project:

### 1. AI SQL Analyst

* **Folder:** `[ai-sql-analyst](ai-sql-analyst)`
* **Description:** This project is an application that uses a Large Language Model (LLM) to convert natural language questions (e.g., "How many users signed up last week?") into executable SQL queries.
* **Focus:** The agent connects to a database, generates the appropriate SQL, executes the query, and returns the answer to the user in plain English.

## Technologies Used

* **Python:** The primary language used for the application logic.
* **Large Language Models (LLMs):** (e.g., Google Gemini, OpenAI GPT-4)
* **Agent Frameworks:** (e.g., LangChain)
* **Database Connectivity:** (e.g., SQLAlchemy)
* **SQL:** The query language used to interact with the database.

## How to Use

1.  **Clone the repository:**
    ```
    git clone [https://github.com/Sahil-Patel180/AI_SQL_AGENT.git](https://github.com/Sahil-Patel180/AI_SQL_AGENT.git)
    ```
2.  **Navigate to the project folder:**
    ```
    cd AI_SQL_AGENT/ai-sql-analyst
    ```
3.  **Install dependencies:**
    * (You may need to create a virtual environment first)
    * `pip install -r requirements.txt` (or as specified in the folder)
4.  **Set up environment:**
    * Create a `.env` file for your API keys (e.g., `GOOGLE_API_KEY`) and database connection string.
5.  **Run the application:**
    * `streamlit run app.py` (or `python app.py`, depending on your project's entry point)
