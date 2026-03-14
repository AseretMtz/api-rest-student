from pydantic import BaseModel
from typing import List

class StudentCreate(BaseModel):
  DNI: str
  nombres: str
  notas:List[int]
  promedio: float