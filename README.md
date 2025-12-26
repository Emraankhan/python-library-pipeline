# Library Data Pipeline v2.0

## Overview
This project is a Python-based data engineering pipeline designed to centralize book inventory from disparate sources. It automates the extraction, transformation, and loading (ETL) of data from local CSV files and the Google Books REST API into a PostgreSQL relational database.

## Core Features
- **ETL Orchestration:** Consolidates data from local file systems and external web services.
- **Relational Storage:** Implements a PostgreSQL backend to manage persistent data.
- **Data Integrity:** Includes a custom deduplication logic that validates incoming records against existing database entries to prevent redundancy.
- **Security:** Utilizes environment variables (.env) and Git ignore-rules to ensure database credentials remain secure and are never exposed in version control.
- **Scalability:** Built with modular Python scripts, allowing for easy expansion to additional data sources.

## Technical Stack
- **Language:** Python 3.x
- **Database:** PostgreSQL
- **Libraries:** Pandas (Data manipulation), SQLAlchemy (ORM/Database connection), Requests (API interaction), Dotenv (Security)

## Project Structure
- `main.py`: The application entry point and command-line interface.
- `scripts/ingestion.py`: Contains the core logic for database connectivity and CSV processing.
- `scripts/api_collector.py`: Manages asynchronous requests to the Google Books API and data normalization.
- `scripts/check_data.py`: A utility script for auditing current database inventory.
- `data/`: Directory for source flat files.

## Installation and Setup

1. **Clone the Repository:**
   git clone https://github.com/Emraankhan/python-library-pipeline.git

2. **Install Dependencies:**
   pip install pandas sqlalchemy psycopg2-binary requests python-dotenv

3. **Environment Configuration:**
   Create a .env file in the root directory and define the connection string:
   DB_CONN_STRING=postgresql://username:password@localhost:5432/database_name

4. **Execution:**
   python main.py