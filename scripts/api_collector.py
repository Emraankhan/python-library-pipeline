import requests
import pandas as pd
from scripts.ingestion import load_data_to_sql
from datetime import datetime
import os

def search_google_books(query):
    print(f"\n--- Searching Google Books for: '{query}' ---")
    
    # 1. THE API CALL
    # We limit results to 5 books to keep it clean
    url = f"https://www.googleapis.com/books/v1/volumes?q={query}&maxResults=1"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if "items" not in data:
            print("No books found for that search term.")
            return

        # 2. EXTRACT DATA FROM JSON
        books_list = []
        for item in data["items"]:
            info = item.get("volumeInfo", {})
            
            # Google gives us a lot of info, we only pick what we need
            title = info.get("title", "Unknown Title")
            authors = info.get("authors", ["Unknown Author"])
            # The date is usually 'YYYY-MM-DD', we just take the first 4 digits (year)
            pub_date = info.get("publishedDate", "0000")
            year = pub_date[:4] if pub_date else "0000"

            books_list.append({
                "title": title,
                "author": authors[0], # Just take the first author
                "year_published": int(year) if year.isdigit() else 0
            })

        # 3. CONVERT TO DATAFRAME
        df_api = pd.DataFrame(books_list)
        print(f"Found {len(df_api)} potential matches online.")

        # 4. SEND TO OUR SHARED LOADER (The Guard)
        result = load_data_to_sql(df_api)
        
        # 5. LOG THE RESULT
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        log_path = os.path.join(project_root, 'logs', 'pipeline_log.txt')
        with open(log_path, "a") as f:
            f.write(f"{datetime.now()} [API Search: {query}]: {result}\n")

    except Exception as e:
        print(f"API Error: {e}")

if __name__ == "__main__":
    # Test run
    search_google_books("Python Programming")