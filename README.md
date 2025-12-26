# Library Data Pipeline System v2.0

A professional-grade Python data pipeline that integrates external APIs, handles local data ingestion, and manages a PostgreSQL database—all fully containerized using Docker.

---

## Key Features

* **Automated Ingestion:** Imports book data from local CSV files into a relational database.
* **API Integration:** Connects to the Google Books API to search and save live book titles and metadata.
* **Relational Database:** Powered by PostgreSQL with SQLAlchemy ORM for robust data management and persistence.
* **Dockerized Environment:** Fully containerized using a custom Dockerfile, ensuring consistent performance across different operating systems.
* **Secure Configuration:** Uses .env files and environment variables to protect sensitive database credentials and API keys.

---

## Technology Stack

| Component      | Technology |
| :---           | :--- |
| Language       | Python 3.9 |
| Database       | PostgreSQL (Relational) |
| Libraries      | Pandas, SQLAlchemy, Psycopg2, Requests |
| Container      | Docker |
| Environment    | Dotenv (Secret Management) |

---

## Installation and Setup

### 1. Prerequisites
* Docker Desktop installed and running.
* PostgreSQL installed locally (if connecting to a local host).

### 2. Environment Configuration
Create a .env file in the root directory and add your connection string:
```text
DB_CONN_STRING=postgresql://your_user:your_password@host.docker.internal:5432/my_library


Note: The address host.docker.internal is used to allow the Docker container to communicate with the PostgreSQL service running on your Windows host.


3. Running with Docker (Recommended)
Build the Image:

docker build -t my-library-app .

Run the Interactive Container:

docker run -it --rm --name library-container my-library-app


Project Structure
main.py - The primary entry point and interactive CLI menu.

scripts/

ingestion.py - Logic for processing CSV files and Google Books API requests.

check_data.py - Inventory reporting and database connection verification.

data/ - Directory for source CSV data.

Dockerfile - Blueprint for building the Docker image.

requirements.txt - Python package dependencies.

.env - (Private) Environment variables and credentials.


Author: Imran Khan

Status: Active Development

