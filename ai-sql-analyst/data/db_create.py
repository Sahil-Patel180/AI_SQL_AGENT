import duckdb
import os

# Resolve paths relative to this file to avoid CWD issues
CURRENT_DIR = os.path.dirname(__file__)
ROOT_DIR = os.path.dirname(CURRENT_DIR)
CSV_PATH = os.path.join(CURRENT_DIR, "bank-full.csv")
DB_PATH = os.path.join(ROOT_DIR, "bank_marketing.duckdb")

# Connect to DuckDB (it will create the file if it doesn't exist)
con = duckdb.connect(DB_PATH)

# Read CSV into DuckDB and create a table
con.execute("""
    CREATE OR REPLACE TABLE bank_marketing AS 
    SELECT * FROM read_csv_auto(?, header=True);
""", [CSV_PATH])

# Verify
print(con.execute("SELECT COUNT(*) FROM bank_marketing").fetchone())

# Close
con.close()