import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
import glob

load_dotenv()

conn_string = os.getenv("DB_CONN_STRING")
engine = create_engine(conn_string)

# This looks specifically in your 'data' folder for ANY csv file
data_folder = "./data"
csv_files = glob.glob(os.path.join(data_folder, "*.csv"))

if not csv_files:
    print(f"❌ ERROR: No CSV files found in {data_folder}. Check the folder!")
else:
    for file in csv_files:
        try:
            print(f"🛠️ Found {file}. Loading to database...")
            df = pd.read_csv(file)
            # This creates the 'inventory' table in library_db
            df.to_sql('inventory', engine, if_exists='replace', index=False)
            print(f"✅ SUCCESS: {file} is now in the database!")
        except Exception as e:
            print(f"❌ ERROR loading {file}: {e}")