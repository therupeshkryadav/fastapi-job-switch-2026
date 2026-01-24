# FastAPI Student Management API

A complete RESTful API for managing student records using FastAPI. This application demonstrates best practices in API development including proper HTTP status codes, data validation, and error handling.

## Features

- ✅ **CRUD Operations** - Create, Read, Update, Delete students
- ✅ **Partial Updates** - Update only the fields you need
- ✅ **Search Functionality** - Find students by ID or name
- ✅ **HTTP Status Codes** - Proper status codes (200, 400, 404, 409)
- ✅ **Data Validation** - Pydantic models for request/response validation
- ✅ **Interactive API Docs** - Swagger UI and ReDoc documentation
- ✅ **Error Handling** - Meaningful error messages with HTTPException

## Prerequisites

- Python 3.8+
- FastAPI
- Uvicorn
- Pydantic v2

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/therupeshkryadav/fastapi-job-switch-2026.git
cd fastapi-job-switch-2026
```

### 2. Create a virtual environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install fastapi uvicorn
```

## Running the Application

### Using Uvicorn with auto-reload
```bash
uvicorn myapi:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at:
- **API Base URL**: http://localhost:8000
- **Swagger UI (Interactive Docs)**: http://localhost:8000/docs
- **ReDoc (Alternative Docs)**: http://localhost:8000/redoc

## API Endpoints

### 1. Get All Students
- **URL**: `/get-all-students`
- **Method**: GET
- **Description**: Retrieve all students with total count
- **Response**: 
```json
{
  "total": 3,
  "students": {
    "1": {"id": 1, "name": "John Doe", "age": 20, "email": "john@example.com"},
    ...
  }
}
```

### 2. Get Student by ID
- **URL**: `/get-student/{student_id}`
- **Method**: GET
- **Description**: Retrieve a specific student by their ID
- **Parameters**: `student_id` (path parameter, required)
- **Success Response** (200):
```json
{"id": 1, "name": "John Doe", "age": 20, "email": "john@example.com"}
```
- **Error Response** (404):
```json
{"detail": "Student not found"}
```

### 3. Search Student by Name
- **URL**: `/get-by-name/?name=John`
- **Method**: GET
- **Description**: Search for a student by name (case-insensitive)
- **Parameters**: `name` (query parameter, required)
- **Success Response** (200):
```json
{"id": 1, "name": "John Doe", "age": 20, "email": "john@example.com"}
```
- **Error Response** (400/404):
```json
{"detail": "Name parameter is required"}
```

### 4. Create Student
- **URL**: `/create-student/{student_id}`
- **Method**: POST
- **Description**: Create a new student
- **Parameters**: `student_id` (path parameter, required)
- **Request Body**:
```json
{
  "name": "Alice Smith",
  "age": 21,
  "email": "alice@example.com"
}
```
- **Success Response** (200):
```json
{
  "message": "Student created successfully",
  "student": {"id": 4, "name": "Alice Smith", "age": 21, "email": "alice@example.com"}
}
```
- **Error Response** (409):
```json
{"detail": "Student with this ID already exists"}
```

### 5. Update Student (Partial Update)
- **URL**: `/update-student/{student_id}`
- **Method**: PUT
- **Description**: Update student fields (only provided fields are updated)
- **Parameters**: `student_id` (path parameter, required)
- **Request Body** (all fields optional):
```json
{
  "name": "Alice Johnson",
  "age": 22
}
```
- **Success Response** (200):
```json
{
  "message": "Student updated successfully",
  "student": {"id": 1, "name": "Alice Johnson", "age": 22, "email": "john@example.com"}
}
```
- **Error Response** (404):
```json
{"detail": "Student not found"}
```

### 6. Delete Student
- **URL**: `/delete-student/{student_id}`
- **Method**: DELETE
- **Description**: Delete a student by their ID
- **Parameters**: `student_id` (path parameter, required)
- **Success Response** (200):
```json
{
  "message": "Student deleted successfully",
  "student": {"id": 1, "name": "John Doe", "age": 20, "email": "john@example.com"}
}
```
- **Error Response** (404):
```json
{"detail": "Student not found"}
```

## HTTP Status Codes

| Code | Meaning |
|------|---------|
| 200 | Success |
| 400 | Bad Request (missing required parameters) |
| 404 | Not Found (student doesn't exist) |
| 409 | Conflict (student ID already exists) |

## Data Models

### Student (Create/Read)
```python
class Student(BaseModel):
    name: str       # Student's full name
    age: int        # Student's age
    email: str      # Student's email address
```

### UpdateStudent (Partial Update)
```python
class UpdateStudent(BaseModel):
    name: Optional[str] = None      # Optional name update
    age: Optional[int] = None       # Optional age update
    email: Optional[str] = None     # Optional email update
```

## Code Highlights

### Key Features Used:
- **Pydantic BaseModel** - Data validation and serialization
- **HTTPException** - Proper error handling with status codes
- **Path Parameters** - Using `Path(...)` for URL parameters
- **Query Parameters** - Optional query strings for search
- **model_dump()** - Modern Pydantic v2 method (replaces deprecated `.dict()`)
- **Partial Updates** - Using `exclude_none=True` for flexible updates

## Example Usage

### Using cURL

Get all students:
```bash
curl http://localhost:8000/get-all-students
```

Get student by ID:
```bash
curl http://localhost:8000/get-student/1
```

Search by name:
```bash
curl "http://localhost:8000/get-by-name/?name=John"
```

Create a new student:
```bash
curl -X POST http://localhost:8000/create-student/4 \
  -H "Content-Type: application/json" \
  -d '{"name":"Alice","age":21,"email":"alice@example.com"}'
```

Update a student:
```bash
curl -X PUT http://localhost:8000/update-student/1 \
  -H "Content-Type: application/json" \
  -d '{"name":"John Updated"}'
```

Delete a student:
```bash
curl -X DELETE http://localhost:8000/delete-student/1
```

## Project Structure

```
fastapi-job-switch-2026/
├── myapi.py           # Main FastAPI application
├── README.md          # This file
└── requirements.txt   # Python dependencies (optional)
```

## Technologies Used

- **FastAPI** - Modern web framework for building APIs
- **Uvicorn** - ASGI web server
- **Pydantic v2** - Data validation and type hints
- **Python 3.8+** - Programming language

## Future Enhancements

- [ ] Database integration (SQLAlchemy, PostgreSQL)
- [ ] Authentication and Authorization
- [ ] Pagination for listing students
- [ ] Input validation (email format, age range)
- [ ] Logging system
- [ ] Unit tests
- [ ] Docker containerization

## License

This project is open source and available under the MIT License.

## Author

Created as a learning project for FastAPI development.
