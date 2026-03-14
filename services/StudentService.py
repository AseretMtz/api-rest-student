from sqlalchemy.orm import Session
from entities.Student import Student
from entities.Student_Notes import Student_Notes  
from domains.Student import StudentCreate
from database.connection import SessionLocal

def get_student(db: Session, student_id: str):
    return db.query(Student).filter(Student.dni == student_id).first()

def get_student_notes(db: Session, student_id: int):
    return db.query(Student_Notes).filter(Student_Notes.alumno_id == student_id).all()

def get_all_information( student_id: str):
    db: Session = SessionLocal()
    try:
        print(f"get information of student {student_id}")
        student = get_student(db, student_id)
        if not student:
            return None
        print(f"Student founded: {student_id}")
        notes = get_student_notes(db, student.id)
        promedio = (sum(n.nota for n in notes) / len(notes)) if notes else None

        return  StudentCreate(
            DNI=student.dni,
            nombres=student.nombres,
            notas=[n.nota for n in notes],
            promedio=promedio
        )

    finally:
        db.close()
