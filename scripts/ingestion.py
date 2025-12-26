import os
import pandas as pd
from dotenv import load_dotenv, find_dotenv
from sqlalchemy import create_engine

# 1. Load Environment Variables
load_dotenv(find_dotenv())
conn_string = os.getenv('DB_CONN_STRING')

# 2. Create Engine - We do this outside the function so it's ready for everyone
if conn_string:
    engine = create_engine(conn_string)
else:
    print("!!! ERROR: DB_CONN_STRING not found in .env !!!")
    engine = None

def load_data_to_sql(df_new):
    """The UNIVERSAL DUPLICATE GUARD."""
    if engine is None:
        return "ERROR: Database engine not initialized."

    try:
        # Clean the input
        df_new['title'] = df_new['title'].str.upper().str.strip()
        
        # Check existing data
        existing_books = pd.read_sql("SELECT title FROM inventory", engine)
        existing_titles = existing_books['title'].tolist()

        # Filter duplicates
        df_to_load = df_new[~df_new['title'].isin(existing_titles)]

        if df_to_load.empty:
            summary = "No new data (Book already exists in library)."
            print(summary)
            return summary
        else:
            count = len(df_to_load)
            df_to_load.to_sql('inventory', engine, if_exists='append', index=False)
            summary = f"SUCCESS: Added {count} new records."
            print(summary) # This ensures you see the result in terminal
            return summary

    except Exception as e:
        error_msg = f"ERROR in Loader: {str(e)}"
        print(error_msg)
        return error_msg


def load_data_to_sql(df_new):
    """
    The UNIVERSAL DUPLICATE GUARD.
    Works for CSV data, API data, or any other source.
    """
    log_msg = ""
    try:
        # Clean the input titles for consistency
        df_new['title'] = df_new['title'].str.upper().str.strip()
        
        # Check existing data
        existing_books = pd.read_sql("SELECT title FROM inventory", engine)
        existing_titles = existing_books['title'].tolist()

        # Filter out duplicates
        df_to_load = df_new[~df_new['title'].isin(existing_titles)]

        if df_to_load.empty:
            summary = "No new data to add. Everything is a duplicate."
            print(summary)
            return summary
        else:
            count = len(df_to_load)
            df_to_load.to_sql('inventory', engine, if_exists='append', index=False)
            summary = f"SUCCESS: Added {count} new records."
            print(summary)
            return summary

    except Exception as e:
        return f"ERROR in Loader: {str(e)}"

def run_csv_ingestion():
    """Specific logic for reading the local CSV file."""
    print("\n--- Starting CSV Ingestion ---")
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    file_path = os.path.join(project_root, 'data', 'books_to_import.csv')
    log_file_path = os.path.join(project_root, 'logs', 'pipeline_log.txt')

    try:
        if not os.path.exists(file_path):
            print(f"File not found: {file_path}")
            return

        df = pd.read_csv(file_path)
        df = df.rename(columns={'year': 'year_published'}) # Map CSV column to SQL column
        
        # USE THE SHARED LOADER
        result = load_data_to_sql(df)
        
        # Logging
        with open(log_file_path, "a") as f:
            f.write(f"{datetime.now()} [CSV]: {result}\n")

    except Exception as e:
        print(f"CSV Error: {e}")

if __name__ == "__main__":
    run_csv_ingestion()