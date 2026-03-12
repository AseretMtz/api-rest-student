from sqlalchemy import Column, Integer, String
from database.connection import Base

class Student(Base):
    __tablename__ = "alumnos"

    id = Column(Integer, primary_key=True, index=True)
    dni = Column(String)
    nombres = Column(String)
    promedio = Column(Integer)