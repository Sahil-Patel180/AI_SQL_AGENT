import re

def is_sql_safe(query: str) -> bool:
    unsafe_patterns = ["DROP", "DELETE", "UPDATE", "INSERT", "ALTER"]
    pattern = re.compile("|".join(unsafe_patterns), re.IGNORECASE)
    return not bool(pattern.search(query))
