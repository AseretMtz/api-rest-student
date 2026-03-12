from sqlalchemy import Column, Integer, ForeignKey,BigInteger
from database.connection import Base

class Student_Notes(Base):
    __tablename__ = "alumno_notas"

    id = Column(BigInteger, primary_key=True, index=True)
    alumno_id = Column(Integer, ForeignKey("alumnos.id"), index=True, nullable=False)
    nota = Column(Integer, nullable=False)