from typing import Dict, List, Optional

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, EmailStr, Field


class StudentBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    age: int = Field(..., ge=1, le=120)
    email: EmailStr


class StudentCreate(StudentBase):
    pass


class StudentUpdate(BaseModel):
    name: Optional[str] = Field(default=None, min_length=2, max_length=100)
    age: Optional[int] = Field(default=None, ge=1, le=120)
    email: Optional[EmailStr] = None


class Student(StudentBase):
    id: int


app = FastAPI(title="Student REST API", version="1.1.0")

_students: Dict[int, Student] = {}
_next_id = 1


def _get_student_or_404(student_id: int) -> Student:
    student = _students.get(student_id)
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.get("/students", response_model=List[Student])
def list_students() -> List[Student]:
    return list(_students.values())


@app.post("/students", response_model=Student, status_code=status.HTTP_201_CREATED)
def create_student(student: StudentCreate) -> Student:
    global _next_id
    created = Student(id=_next_id, **student.model_dump())
    _students[_next_id] = created
    _next_id += 1
    return created


@app.get("/students/{student_id}", response_model=Student)
def get_student(student_id: int) -> Student:
    return _get_student_or_404(student_id)


@app.put("/students/{student_id}", response_model=Student)
def update_student(student_id: int, payload: StudentUpdate) -> Student:
    existing = _get_student_or_404(student_id)
    updated_data = payload.model_dump(exclude_none=True)
    updated = existing.model_copy(update=updated_data)
    _students[student_id] = updated
    return updated


@app.delete("/students/{student_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_student(student_id: int) -> None:
    _get_student_or_404(student_id)
    del _students[student_id]
