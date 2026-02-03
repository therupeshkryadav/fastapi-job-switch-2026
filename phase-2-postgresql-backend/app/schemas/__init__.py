from pydantic import BaseModel
from typing import Optional

class StudentBase(BaseModel):
    name: str
    age: int
    email: str

class StudentCreate(StudentBase):
    pass

class StudentUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    email: Optional[str] = None

class Student(StudentBase):
    id: int

    class Config:
        from_attributes = True