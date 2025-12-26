from scripts.ingestion import run_csv_ingestion
from scripts.api_collector import search_google_books
import subprocess
import os

def run_pipeline():
    # This loop keeps the program running
    while True:
        print("\n========================================")
        print("   LIBRARY DATA PIPELINE SYSTEM v2.0    ")
        print("========================================")
        print("1. Import from CSV (data/books_to_import.csv)")
        print("2. Search Google Books (API)")
        print("3. View Current Inventory")
        print("4. Exit Program")
        
        choice = input("\nEnter choice (1/2/3/4): ").strip()

        if choice == '1':
            run_csv_ingestion()
        
        elif choice == '2':
            keyword = input("Enter book title or keyword to search: ")
            search_google_books(keyword)
        
        elif choice == '3':
            script_path = os.path.join('scripts', 'check_data.py')
            if os.path.exists(script_path):
                subprocess.run(['python', script_path])
            else:
                print("Error: scripts/check_data.py not found.")
        
        elif choice == '4':
            print("\nShutting down pipeline. Goodbye!")
            break  # This exits the 'while' loop and ends the program
        
        else:
            print("\n[!] Invalid choice. Please pick 1, 2, 3, or 4.")

        # Optional: Pause for a second so the user can read the output
        input("\nPress Enter to return to the main menu...")

if __name__ == "__main__":
    run_pipeline()