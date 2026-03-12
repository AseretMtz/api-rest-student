from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.orm import Session
from services.StudentService import get_all_information
from database.connection import get_db

router = APIRouter(prefix="/api/v1/alumnos", tags=["Students"])

@router.get("/{student_id}")
def get(student_id: str, db: Session = Depends(get_db)):
    data = get_all_information(db, student_id)
    if data is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return data

