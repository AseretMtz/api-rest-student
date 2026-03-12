from entities.Student import Student

def get_student(db, student_id:String):
    return db.query(Student).filter(Student.dni == student_id).first()