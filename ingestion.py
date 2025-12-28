import os
import pandas as pd
from datetime import datetime
from sqlalchemy import create_engine
from dotenv import load_dotenv, find_dotenv

# 1. Setup Environment & Database
load_dotenv(find_dotenv())
conn_string = os.getenv('DB_CONN_STRING')

if not conn_string:
    print("!!! ERROR: DB_CONN_STRING not found !!!")
    engine = None
else:
    engine = create_engine(conn_string)

def load_data_to_sql(df_new):
    """Universal loader that prevents duplicate book titles."""
    if engine is None: return "ERROR: No Database Connection"

    try:
        # Standardize titles for comparison
        df_new['title'] = df_new['title'].str.upper().str.strip()
        
        # Get existing titles from DB to prevent duplicates
        existing_books = pd.read_sql("SELECT title FROM inventory", engine)
        existing_titles = existing_books['title'].tolist()

        # Only keep rows where the title isn't already in the database
        df_to_load = df_new[~df_new['title'].isin(existing_titles)]

        if df_to_load.empty:
            return "No new data (All books were duplicates)."
        
        # Load the unique records
        count = len(df_to_load)
        df_to_load.to_sql('inventory', engine, if_exists='append', index=False)
        return f"SUCCESS: Added {count} new records."

    except Exception as e:
        return f"DATABASE ERROR: {str(e)}"

def process_csv(file_path):
    """
    Main entry point for the Automator.
    This function is what 'automator.py' calls when a file is detected.
    """
    print(f"🛠️  Processing file: {os.path.basename(file_path)}")
    
    try:
        # Load the CSV
        df = pd.read_csv(file_path)
        
        # Data Mapping: Ensure CSV columns match our SQL table
        # If your CSV uses 'year', rename it to 'year_published'
        if 'year' in df.columns:
            df = df.rename(columns={'year': 'year_published'})

        # Run the loader
        result = load_data_to_sql(df)
        print(f"📊 Result: {result}")

        # Logging (Optional but recommended for professional pipelines)
        log_dir = os.path.join(os.getcwd(), 'logs')
        if not os.path.exists(log_dir): os.makedirs(log_dir)
        
        with open(os.path.join(log_dir, 'pipeline.log'), "a") as f:
            f.write(f"{datetime.now()} | {os.path.basename(file_path)} | {result}\n")

    except Exception as e:
        print(f"❌ Ingestion Failed: {e}")

if __name__ == "__main__":
    # This allows you to still run the script manually for testing
    test_path = os.path.join('data', 'books.csv')
    if os.path.exists(test_path):
        process_csv(test_path)