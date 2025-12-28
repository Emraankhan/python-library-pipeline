# 📚 Library Data Pipeline System v2.0

A professional-grade Python data engineering pipeline that automates ingestion from local sources to a PostgreSQL warehouse, featuring real-time file monitoring and a Business Intelligence (BI) layer.

---

## 🚀 Key Features

* **Event-Driven Ingestion:** Uses `watchdog` to monitor the `./data` directory and automatically trigger loads when new CSV files are detected.
* **API Integration:** Connects to the Google Books API to enrich book metadata and fetch live titles.
* **Relational Database:** Powered by **PostgreSQL** with **SQLAlchemy ORM** for robust data management and persistence.
* **Dockerized Environment:** Fully containerized PostgreSQL service, ensuring consistent performance across different operating systems.
* **BI & Visualization:** Integrated with **Metabase** for real-time dashboards, inventory reporting, and SQL-based analytics.
* **Secure Configuration:** Managed via `.env` files to protect sensitive database credentials and API keys.

---

## 🛠️ Technology Stack

| Component      | Technology |
| :---           | :--- |
| **Language** | Python 3.12 |
| **Database** | PostgreSQL (Relational) |
| **Automation** | Watchdog (File System Observer) |
| **Libraries** | Pandas, SQLAlchemy, Psycopg2, Requests |
| **Container** | Docker |
| **BI Tool** | Metabase |

---

## 🏗️ System Architecture



1.  **Source:** CSV files are dropped into the `./data` folder.
2.  **Orchestrator:** `automator.py` detects the file and triggers the ingestion logic.
3.  **Storage:** Data is cleaned via Pandas and pushed to the `inventory` table in PostgreSQL.
4.  **Analytics:** Metabase syncs with the DB to provide visual insights.

---

## ⚙️ Installation and Setup

### 1. Prerequisites
* **Docker Desktop** installed and running.
* **Python 3.10+** installed locally.

### 2. Environment Configuration
Create a `.env` file in the root directory:
```text
DB_CONN_STRING=postgresql://postgres:your_password@host.docker.internal:5432/library_db


Note: The address host.docker.internal is used to allow the Python script to communicate with the PostgreSQL service running inside Docker from your Windows host.

### 3. Running the Pipeline
**Start the Database:**
docker start library-db

**Launch the Automator:**
python automator.py

##📂 Project Structure

.
├── automator.py            # Event-driven watcher for real-time ingestion
├── load_data.py            # Manual bulk-load script for troubleshooting
├── main.py                 # Application entry point and interactive CLI
├── scripts/
│   ├── ingestion.py        # CSV ingestion and Google Books API logic
│   └── check_data.py       # Database checks and inventory reporting
├── data/                   # Landing zone for source CSV files
│   └── archived/           # Successfully processed files are moved here
├── Dockerfile              # Container configuration
├── requirements.txt        # Python dependencies
└── .env                    # Environment variables (Private)

Author: Imran Khan

Status: Project 1 (Local Pipeline) - Complete ✅

