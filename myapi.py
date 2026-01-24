# FastAPI Student Management API
from fastapi import FastAPI, Path, HTTPException
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

# ==================== DATA MODELS ====================

class Student(BaseModel):
    """Student data model for request/response validation"""
    name: str
    age: int
    email: str

class UpdateStudent(BaseModel):
    """Partial update model - all fields are optional"""
    name: Optional[str] = None
    age: Optional[int] = None
    email: Optional[str] = None

# ==================== DATABASE ====================

# In-memory student storage (simulates a database)
students = {
    1: {"id": 1, "name": "John Doe", "age": 20, "email": "john@example.com"},
    2: {"id": 2, "name": "Jane Smith", "age": 21, "email": "jane@example.com"},
    3: {"id": 3, "name": "Bob Johnson", "age": 19, "email": "bob@example.com"}
}

# ==================== ENDPOINTS ====================

@app.get("/")
def index():
    """Welcome endpoint"""
    return {"message": "Student Management API"}

@app.get("/get-all-students")
def get_all_students():
    """Retrieve all students with total count"""
    return {"total": len(students), "students": students}

@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(..., description="Student ID")):
    """Get a specific student by ID"""
    if student_id in students:
        return students[student_id]
    raise HTTPException(status_code=404, detail="Student not found")

@app.get("/get-by-name/")
def get_by_name(name: Optional[str] = None):
    """Search student by name (case-insensitive)"""
    if not name:
        raise HTTPException(status_code=400, detail="Name parameter is required")
    
    for student in students.values():
        if student["name"].lower() == name.lower():
            return student
    raise HTTPException(status_code=404, detail="Student not found")

@app.post("/create-student/{student_id}")
def create_student(student: Student, student_id: int = Path(..., description="Student ID")):
    """Create a new student"""
    if student_id in students:
        raise HTTPException(status_code=409, detail="Student with this ID already exists")
    
    students[student_id] = student
    return {"message": "Student created successfully", "student": students[student_id]}

@app.put("/update-student/{student_id}")
def update_student(student: UpdateStudent, student_id: int = Path(..., description="Student ID")):
    """
    Update student with partial fields (only provided fields are updated).
    Example: {"name": "Alice"} updates only the name field.
    """
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")
    
    # Using model_dump(exclude_none=True) - recommended method in Pydantic v2
    # (replaces deprecated .dict() method for better compatibility)
    existing = students[student_id]
    update_data = student.model_dump(exclude_none=True)
    existing.update(update_data)
    students[student_id] = existing
    
    return {"message": "Student updated successfully", "student": students[student_id]}

@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int = Path(..., description="Student ID")):
    """Delete a student by ID"""
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")
    
    deleted_student = students.pop(student_id)
    return {"message": "Student deleted successfully", "student": deleted_student}

