# Import necessary modules from FastAPI
from fastapi import FastAPI, Path

# Create a FastAPI application instance
app = FastAPI()

# Sample student data dictionary with student ID as key
students = {
    1: {
        "name": "John Doe",
        "age": 21,
        "year": "Year 12"  
    },
    2: {
        "name": "Jane Smith",
        "age": 22,
        "year": "Year 13"  
    }
}

# Root endpoint that returns basic greeting
@app.get("/")
def index():
    return {"name": "First Data"}

# Endpoint to get a specific student by ID
# student_id must be between 1 and 2 (gt=0, lt=3)
@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(..., description="The ID of the student you want to get", gt=0, lt=3)):
    return students[student_id]

# Endpoint to get a student by name using query parameter
@app.get("/get-by-name")
def get_student_by_name(name: str = None):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data": "Not Found"}