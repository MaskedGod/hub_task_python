# URL Shortener Service

A FastAPI-based URL shortening service with PostgreSQL backend and external data integration capabilities.

## Features

- URL shortening with collision detection
- Redirect to original URLs
- Asynchronous external resourse data fetching
- PostgreSQL database for persistent storage
- Modern async SQLAlchemy ORM
- FastAPI with automatic OpenAPI documentation


## Project Structure

```plaintext
├── src/
│   ├── api/           # API routes and endpoints
│   ├── config/        # Configuration management
│   ├── db/           # Database models and connection
│   ├── repositories/ # Data access layer
│   └── services/     # Business logic layer
├── migrations/       # Alembic database migrations
├── main.py          # Application entry point
└── alembic.ini      # Alembic configuration
```
## Prerequisites

- Python 3.12+
- PostgreSQL

### Dependencies

Key dependencies:

- FastAPI - Web framework
- SQLAlchemy - ORM
- Alembic - Database migrations
- Pydantic - Data validation
- HTTPX - Async HTTP client

## Installation

### 1. Dependencies Installation

Choose one of the following methods:

#### Option A: Using pip

```bash
pip install -r requirements.txt
```

#### Option B: Using UV (Faster alternative)

```bash
pip install uv
uv venv
uv pip sync requirements.txt
```

### 2. Environment Setup

1. Copy the environment template:

```bash
copy .env.example .env
```

2. Update `.env` with your PostgreSQL credentials:

```plaintext
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASS=your_password
DB_PORT=5432
DB_HOST=localhost
BASE_URl=http://127.0.0.1:8080/urls
```

### 3. Database Setup

1. Ensure PostgreSQL is running

2. Create database using one of these methods:

a. Using pgAdmin (Recommended for Windows):

- Open pgAdmin
- Right-click on "Databases"
- Select "Create" > "Database"
- Enter your database name
- Click "Save"

b. Using psql command line:

```bash
psql -U postgres
CREATE DATABASE your_db_name;
```

3. Run migrations:

```bash
alembic upgrade head
```

## Running the Application

Start the development server:

```bash
uvicorn main:app --reload
```

The service will be available at `http://127.0.0.1:8080`

## API Endpoints

### 1. Shorten URL

- **POST** `/urls/`
  ```json
  {
    "url": "https://example.com/very/long/url"
  }
  ```
  Returns:
  ```json
  {
    "short_url": "http://127.0.0.1:8080/urls/abc123"
  }
  ```

### 2. Redirect to Original URL

- **GET** `/urls/{short_id}`
  - Redirects to the original URL with status code 307
  - Example: `http://127.0.0.1:8080/urls/abc123`

### 3. External Data

- **GET** `/external-data/?url={url}`
  - Fetches data from external resourses asynchronously
  - Example: `/external-data/?url=https://example.com/data`


