from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from domains.Student import StudentCreate
from services.StudentService import get_student
from database.connection import get_db

router = APIRouter(prefix="/api/v1/alumnos", tags=["Students"])

@router.get("/{student_id}")
def get(student_id: str, db: Session = Depends(get_db)):
    return get_student(db, student_id)


