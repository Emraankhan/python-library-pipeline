import time
import os
from watchdog.observers.polling import PollingObserver as Observer  # <--- CHANGE THIS LINE
from watchdog.events import FileSystemEventHandler
from ingestion import process_csv 

WATCH_PATH = "./data"
ARCHIVE_PATH = "./data/archived"


# Ensure the archive folder exists
if not os.path.exists(ARCHIVE_PATH):
    os.makedirs(ARCHIVE_PATH)

class DataHandler(FileSystemEventHandler):
    def on_created(self, event):
        # We only care about new CSV files
        if not event.is_directory and event.src_path.endswith('.csv'):
            filename = os.path.basename(event.src_path)
            print(f"📁 New Data Detected: {filename}")
            
            # Pause to ensure the file is fully saved
            time.sleep(1) 
            
            try:
                # 1. Run Ingestion
                process_csv(event.src_path)
                
                # 2. Archive (Move file to prevent re-processing)
                os.rename(event.src_path, os.path.join(ARCHIVE_PATH, filename))
                print(f"✅ Successfully processed and archived: {filename}")
            except Exception as e:
                print(f"❌ Error processing {filename}: {e}")

if __name__ == "__main__":
    event_handler = DataHandler()
    observer = Observer()
    observer.schedule(event_handler, WATCH_PATH, recursive=False)
    
    print(f"🚀 Watcher Active: Monitoring {WATCH_PATH}...")
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
    