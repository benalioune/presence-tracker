
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