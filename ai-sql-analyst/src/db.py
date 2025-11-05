import duckdb

DB_PATH = "bank_marketing.duckdb"

def get_connection():
    return duckdb.connect(DB_PATH)

def execute_query(query: str):
    con = get_connection()
    try:
        df = con.execute(query).df()
        return df
    finally:
        con.close()

def get_db_metadata():
    """Return database name, tables, and columns."""
    con = get_connection()
    try:
        db_name = DB_PATH.split("/")[-1]
        tables = con.execute("SHOW TABLES").fetchall()
        table_info = {}
        for (table_name,) in tables:
            cols = con.execute(f"PRAGMA table_info({table_name})").fetchdf()["name"].tolist()
            table_info[table_name] = cols
        return db_name, table_info
    finally:
        con.close()