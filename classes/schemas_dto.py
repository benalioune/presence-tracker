
from pydantic import BaseModel


# DTO : Data Transfert Object ou Schema
# Représente la structure de la données (data type) en entrée ou en sortie de notre API.
# Model Pydantic = Datatype

class StudentNoID(BaseModel):
    name: str


class Student(BaseModel):
    id: str
    name: str
    
    
class User(BaseModel):

    email: str
    password: str
    

class UserLogin(BaseModel):

    email: str
    password: str
    
# define how we except the request body to be
class Config:
    schema_extra={
        "exemple": {
            "email": "benalioune6@gmail.com",
            "password": "abcdef"
        }
    }
    

class Sessions (BaseModel):
    id: str
    idStudent: str
    idCourse: str
    date: str
    sale: str

class Config:
    schema_extra={
        "exemple": {
            "email": "benalioune6@gmail.com",
            "password": "pass"
        }
    }
    
    
users = [
    
    User(email="benalioune6@gmail.com", password="pass")
    
]
    

students = [
    Student(id="efe", name="Adama"),
    Student(id="fef", name="Adrien"),
    Student(id="dfd", name="Akbar"),
    Student(id="frf", name="Alioune")
]



class CourseNoId (BaseModel):
    courseName: str
    coursePrice: float
    courseTeacher: str
    courseWording: str
    courseDuration: int





class Course(BaseModel): 
    id: str
    courseWording: str
    coursePrice: float
    courseTeacher: str
    courseDuration: int
    
    
courses = [
    Course(id="shsj", courseWording="Mathématiques", coursePrice=50.0, courseTeacher="M. Smith", courseDuration=60),
    Course(id="gsgs", courseWording="Physique", coursePrice=60.0, courseTeacher="Mme. Johnson", courseDuration=45),
    Course(id="gsh", courseWording="chimie", coursePrice=60.0, courseTeacher="Mme. Berry", courseDuration=45)
    
]


