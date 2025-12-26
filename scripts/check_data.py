import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Get the connection string from the environment
conn_string = os.getenv('DB_CONN_STRING')
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