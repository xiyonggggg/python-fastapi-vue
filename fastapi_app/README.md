# Python FastAPI Backend
This is a FastAPI backend written in Python that demonstrates a simple CRUD (Create, Read, Update, Delete) application.
The project uses PostgreSQL as the database, managed with SQLAlchemy ORM, and can be run either locally or inside Docker.

## Project Features
- RESTful API built with FastAPI
- PostgreSQL integration
- Dockerized for easy deployment
- Interactive API docs with Swagger (/docs) and ReDoc (/redoc)

## Prerequisites
- Python 3.12+

## Getting Started
Create virtual environment & install dependencies:
```
python -m venv fastapi_env

# Windows
fastapi_env\Scripts\activate
# Linux / Mac
source fastapi_env/bin/activate

pip install -r requirements.txt
```

Run the server
```
uvicorn src.main:app --host 0.0.0.0 --port 5000 --reload
```

API will be available at: http://localhost:5000

__Note__: make sure you have your postgresdb docker running.

## Running with Docker
//trainee task