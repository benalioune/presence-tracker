from datetime import datetime
from pydantic import BaseModel

# DTO : Data Transfert Object ou Schema
# Représente la structure de la données (data type) en entrée ou en sortie de notre API.
# Model Pydantic = Datatype

class StudentNoID(BaseModel):
    name: str


class Student(BaseModel):
    id: int
    name: str
    
    

students = [
    Student(id=1, name="Adama"),
    Student(id=2, name="Adrien"),
    Student(id=3, name="Akbar")
]
