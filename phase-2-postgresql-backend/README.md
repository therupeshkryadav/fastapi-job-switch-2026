# Phase 2: PostgreSQL Backend

This phase implements a FastAPI backend with PostgreSQL database for student management.

## Features

- RESTful API for student CRUD operations
- PostgreSQL database integration
- Pydantic schemas for validation
- SQLAlchemy ORM for database operations
- Docker containerization
- Docker Compose for local development

## Setup

### Using Docker Compose (Recommended)

1. Ensure Docker and Docker Compose are installed
2. Run the application:
   ```bash
   docker-compose up --build
   ```
3. The API will be available at http://localhost:8000
4. PostgreSQL database at localhost:5432

### Manual Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Set up PostgreSQL database and update DATABASE_URL in environment

3. Run the application:
   ```bash
   uvicorn app.main:app --reload
   ```

## API Endpoints

- `GET /` - Welcome message
- `GET /students/` - List all students (with pagination)
- `GET /students/{student_id}` - Get student by ID
- `POST /students/` - Create a new student
- `PUT /students/{student_id}` - Update student
- `DELETE /students/{student_id}` - Delete student

## API Documentation

When running, visit http://localhost:8000/docs for interactive Swagger UI documentation.

## Database Schema

The `students` table has the following columns:
- `id` (Integer, Primary Key)
- `name` (String)
- `age` (Integer)
- `email` (String, Unique)