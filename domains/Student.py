from pydantic import BaseModel

class StudentCreate(BaseModel):
  DNI: str
  nombres: str
  notas:List[float]
  promedio: int