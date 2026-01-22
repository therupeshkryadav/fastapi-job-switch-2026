# fastapi-job-switch-2026

## Overview
A FastAPI application demonstrating basic REST API endpoints for managing student data.

## Features
- ✅ Root endpoint returning basic greeting
- ✅ Get student by ID with path parameter validation (IDs 1-2)
- ✅ Get student by name using query parameter
- ✅ Sample student database with 2 records
- ✅ Comprehensive code comments and documentation

## Endpoints

### 1. Root Endpoint
- **URL:** `/`
- **Method:** GET
- **Response:** Basic greeting message

### 2. Get Student by ID
- **URL:** `/get-student/{student_id}`
- **Method:** GET
- **Parameters:** 
  - `student_id` (path): Integer between 1-2 (required)
- **Response:** Student object with name, age, and year

### 3. Get Student by Name
- **URL:** `/get-by-name`
- **Method:** GET
- **Parameters:**
  - `name` (query): Student name (optional)
- **Response:** Student object or "Not Found" message

## Getting Started

### Prerequisites
- Python 3.7+
- FastAPI
- Uvicorn

### Installation
```bash
pip install fastapi uvicorn
```

### Running the Application
```bash
uvicorn myapi:app --reload
```

The API will be available at `http://localhost:8000`

### API Documentation
- Interactive API docs (Swagger UI): `http://localhost:8000/docs`
- Alternative API docs (ReDoc): `http://localhost:8000/redoc`

## Sample Data
The application includes 2 pre-loaded students:
1. **John Doe** - Age 21, Year 12
2. **Jane Smith** - Age 22, Year 13

## Progress
- [x] Created FastAPI application instance
- [x] Implemented root endpoint
- [x] Added get student by ID endpoint with validation
- [x] Added get student by name endpoint
- [x] Added comprehensive code comments
- [x] Documented all endpoints
- [x] Created README documentation