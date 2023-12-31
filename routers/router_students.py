
from fastapi import APIRouter, Depends, HTTPException, status
from classes.schemas_dto import students
from classes.schemas_dto import Student
from classes.schemas_dto  import StudentNoID
from typing import List
from routers.router_auth import get_current_user

from database.firebase import db



import uuid



router = APIRouter(
    prefix='/students',
    tags=['Students']
)


# Verbs + Endpoints
@router.get("/students", response_model=List[Student])
async def get_student(user_data: int= Depends(get_current_user)):
    queryResults = db.child("student").get(user_data['idToken']).val()
    if not queryResults : return []
    studentArray = [Student(**value) for value in queryResults.values()]
    return studentArray 




# 1. Exercice (10min) Create new Student: POST
# response_model permet de définir de type de réponse (ici nous retournons le student avec sont id)
# status_code est définit sur 201-Created car c'est un POST
@router.post('/students', response_model=Student, status_code=201)
async def create_student(givenName:str):
    # génération de l'identifiant unique
    generatedId=uuid.uuid4()
    # création de l'object/dict Student 
    newStudent= Student(id=str(generatedId), name=givenName)
    # Ajout du nouveau Student dans la List/Array
    students.append(newStudent)
    
    db.child("student").child(generatedId).set(newStudent.model_dump())
    # Réponse définit par le Student avec son ID
    return newStudent


# 2. Exercice (10min) Student GET by ID
# response_model est un Student car nous souhaitons trouvé l'étudiant correspodant à l'ID
@router.get('/students/{student_id}', response_model=Student)
async def get_student_by_id(student_id: str, user_data: int= Depends(get_current_user)):
    queryResult = db.child('student').child(student_id).get(user_data['idToken']).val()
    if not queryResult : raise HTTPException(status_code=404, detail="Student not found") 
    return queryResult




# 3. Exercice (10min) PATCH Student (name)
@router.patch('/{student_id}', status_code=204)
async def student_update(student_id: str, student: StudentNoID, user_data: int= Depends(get_current_user)):
    queryResult = db.child('student').child(student_id).get(user_data['idToken']).val()
    if not queryResult : raise HTTPException(status_code=404, detail="Student not found") 
    updatedStudent = Student(id=student_id, **student.model_dump())
    return db.child('student').child(student_id).update(data=updatedStudent.model_dump(), token=user_data['idToken'])


# 4. Exercice (10min) DELETE Student
@router.delete("/{student_id}", status_code=202, response_model=str)
async def student_delete(student_id: str, user_data: int= Depends(get_current_user)) :
    queryResult = db.child('student').child(student_id).get(user_data['idToken']).val()
    if not queryResult : 
        raise HTTPException(status_code=404, detail="Student not found")
    db.child('student').child(student_id).remove(token=user_data['idToken'])
    return "Student deleted"

# Reste à faire 
# - Sortir mon student's router dans un dossier "routers"
# - Rédiger une documentation et l'ajouter à mon app FastAPI()
# - Sortir mes pydantic models dans un dossier classes
# - Ajouter les tags 
