import duckdb
import os

# Resolve DB path relative to repo root to avoid hardcoded absolute paths
CURRENT_DIR = os.path.dirname(__file__)
ROOT_DIR = os.path.dirname(CURRENT_DIR)
DB_PATH = os.path.join(ROOT_DIR, "bank_marketing.duckdb")
CSV_PATH = os.path.join(CURRENT_DIR, "bank-full.csv")

con = duckdb.connect(DB_PATH)

# Ensure the source table exists (idempotent setup)
exists = con.execute(
    """
    SELECT COUNT(*)
    FROM information_schema.tables
    WHERE table_name = 'bank_marketing'
    """
).fetchone()[0]

if exists == 0:
    con.execute(
        """
        CREATE TABLE bank_marketing AS
        SELECT * FROM read_csv_auto(?, header=True)
        """,
        [CSV_PATH],
    )
df = con.execute("""
    SELECT *
    FROM bank_marketing
    LIMIT 5;
""").df()

print(df)
con.close()