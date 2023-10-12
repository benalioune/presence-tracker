from datetime import datetime
from pydantic import BaseModel
from typing import List

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
    Student(id=3, name="Akbar"),
    Student(id=4, name="Alioune")
]



class Courses_POST_Body (BaseModel):
    courseName: str
    coursePrice: float
    courseTeacher: str
    courseWording: str
    courseDuration: int





class Course(BaseModel): 
    id: int
    courseWording: str
    coursePrice: float
    courseTeacher: str
    courseDuration: int
    
courses = [
    Course(id=1, courseWording="Mathématiques", coursePrice=50.0, courseTeacher="M. Smith", courseDuration=60),
    Course(id=2, courseWording="Physique", coursePrice=60.0, courseTeacher="Mme. Johnson", courseDuration=45),
    Course(id=3, courseWording="chimie", coursePrice=60.0, courseTeacher="Mme. Berry", courseDuration=45)
    
]