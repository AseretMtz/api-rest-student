from fastapi import APIRouter, Depends,HTTPException
from services.StudentService import get_all_information

router = APIRouter(prefix="/api/v1/alumnos", tags=["Students"])

@router.get("/{student_id}")
def get(student_id: str):
    data = get_all_information(student_id)
    if data is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return data

