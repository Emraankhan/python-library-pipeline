import pandas as pd
from sqlalchemy import create_engine

# Using the same engine style as ingestion.py
conn_string = 'postgresql://postgres:emraan123@localhost:5432/my_library'
engine = create_engine(conn_string)

def verify_inventory():
    print("\n--- LIBRARY SUMMARY REPORT ---")
    
    # This query sorts by title so you can easily spot duplicates
    query = "SELECT * FROM inventory ORDER BY title ASC"
    
    # Passing 'engine' instead of 'conn' removes the UserWarning
    df = pd.read_sql(query, engine)
    
    if df.empty:
        print("Inventory is currently empty.")
    else:
        print(f"Total Books: {len(df)}")
        print(df.to_string(index=False))

if __name__ == "__main__":
    verify_inventory()