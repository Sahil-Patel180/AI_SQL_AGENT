# AI SQL Analyst

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A production-ready sub-agent of **AI_SQL_AGENT** for natural-language SQL analysis and insights.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [System Architecture](#system-architecture)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Application](#running-the-application)
- [Example Flow](#example-flow)
- [Configuration](#configuration)

## Overview

The **ai-sql-analyst** module allows you to ask business-style questions (in plain English) about your SQL database—such as:  
> “What’s the average loan amount by region for approved loans in 2024?”  
It then intelligently translates your question into SQL, executes it against your configured database, and returns structured results for further analysis or visualization.

This module is crafted for data analysts, BI engineers and developers seeking conversational access to relational data without writing raw SQL queries.

## Features

- Natural-language input → SQL translation  
- Support for SQL-compliant databases via configurable connector (e.g., PostgreSQL, MySQL, SQLite)  
- Execution of derived SQL queries with safe parameterisation  
- Results returned in formats suitable for data-analysis workflows (table, CSV, JSON)  
- Modular architecture: translation, execution, formatting layers  
- Designed for production readiness: logging, error handling, configuration, extensibility  
- Easily embed into dashboards, notebooks, apps or conversational interfaces

## System Architecture

1. **User Input** — Enter your question in natural language.  
2. **Translator Module** — Converts the question into a valid SQL query, abiding by schema and syntax constraints.  
3. **Executor Module** — Connects to your database, runs the query, manages timeouts and safety.  
4. **Formatter Module** — Converts results into desired format (dataframe/table/JSON/CSV).  
5. **Optional Integration** — Hook into web UI (Streamlit/Flask), schedule analysis, or embed into chatbots.

## Getting Started

### Prerequisites  
- Python 3.8 or newer  
- A SQL database (PostgreSQL, MySQL, SQLite or similar) accessible with credentials  
- Configure appropriate database-connection string  
- Optionally: if using an LLM or external model for translation, provide API key or model credentials  
- Recommended: virtual environment (`venv`, `conda`, etc.)  

### Installation  
```
git clone https://github.com/Sahil-Patel180/AI_SQL_AGENT.git
cd AI_SQL_AGENT/ai-sql-analyst
python -m venv venv
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
pip install -r requirements.txt
````

### Running the Application

```
python main.py
```

Then type your question:

```
> “Show the number of approved loans by region for Q1 2025.”
```

The module will translate, query, and output results.

## Example Flow

**Natural-language input:**

> *“Break down total sales by product category in 2024, and show average order value by month.”*
> **Generated SQL (illustrative):**

```sql
SELECT
  category,
  date_trunc('month', order_date) AS month,
  COUNT(*) AS total_orders,
  AVG(order_value) AS avg_order_value
FROM orders
WHERE order_date BETWEEN '2024-01-01' AND '2024-12-31'
GROUP BY category, month
ORDER BY category, month;
```

**Output:**

```
category     | month     | total_orders | avg_order_value
-------------|-----------|--------------|-----------------
Electronics  | 2024-01   | 1250         | 299.45
Electronics  | 2024-02   | 1130         | 315.22
Home & Garden| 2024-01   | 850          | 185.90
...
```

> *Actual SQL will vary according to your database schema and table names.*

## Configuration

* Copy the sample config (e.g., `config.sample.yaml` or `.env.sample`) → `config.yaml` / `.env`
* Fill in values, for example:

  ```yaml
  DATABASE_URL: "postgresql://user:password@host:port/dbname"
  DEFAULT_SCHEMA: "public"
  QUERY_TIMEOUT: 30  # seconds
  OUTPUT_FORMAT: "json"  # or "table", "csv"
  ```
* If you are using a translation engine (LLM), add the key:

  ```yaml
  MODEL_API_KEY: "your-api-key"
  TRANSLATION_ENGINE: "openai"  # or your custom model
  ```

### 🔹 Author

**Sahil Patel**
*BCA Data Science Student | Data Analyst Enthusiast*
📍 SRM Institute of Science and Technology
🔗 [GitHub: Sahil-Patel180](https://github.com/Sahil-Patel180)

> *“The best question unlocks the deepest insight.”*
> Happy querying & exploring your data! 🎉
