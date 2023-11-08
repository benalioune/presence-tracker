from fastapi import APIRouter, Depends, HTTPException, status
from classes import  schemas_dto
from classes.schemas_dto import courses
from classes.schemas_dto import Course
from classes.schemas_dto  import CourseNoId
from typing import List
import uuid



router = APIRouter(
    prefix='/courses',
    tags=['/Courses']
)


from fastapi import APIRouter, Depends, HTTPException, status
from classes.schemas_dto import courses
from classes.schemas_dto import Student
from classes.schemas_dto  import StudentNoID
from typing import List
from routers.router_auth import get_current_user

from database.firebase import db



import uuid




router = APIRouter(
    prefix='/courses',
    tags=['Courses']
)




@router.get("/courses", response_model=List[Course])
async def get_courses(user_data: int= Depends(get_current_user)):
    queryResults = db.child("course").get(user_data['idToken']).val()
    if not queryResults : return []
    courseArray = [Course(**value) for value in queryResults.values()]
    return courseArray 


@router.post('/courses', response_model=Course, status_code=201)
async def create_Course(nameCourse: str, price: float, teacher: str, duration: int):
    # génération de l'identifiant
    generatedId=uuid.uuid4()
    # création de l'object/dict Course
    newCourse= Course(id=str(generatedId), courseWording=nameCourse, coursePrice=price, courseTeacher=teacher, courseDuration=duration)
    # Ajout du nouveau cours dans la List/Array
    courses.append(newCourse)
    
  
    
    db.child("course").child(str(generatedId)).set(newCourse.model_dump())
    # Réponse définit par le course avec son ID
    return newCourse



@router.get('/courses/{course_id}', response_model=Course)
async def get_course_by_id(course_id: str, user_data: int= Depends(get_current_user)):
    queryResult = db.child('course').child(course_id).get(user_data['idToken']).val()
    if not queryResult : raise HTTPException(status_code=404, detail="Course not found") 
    return queryResult

@router.patch('/{course_id}', status_code=204)
async def course_update(course_id: str, course: CourseNoId, user_data: int= Depends(get_current_user)):
    queryResult = db.child('course').child(course_id).get(user_data['idToken']).val()
    if not queryResult : raise HTTPException(status_code=404, detail="Course not found") 
    updateCourse = Course(id=course_id, **course.model_dump())
    return db.child('course').child(course_id).update(data=updateCourse.model_dump(), token=user_data['idToken'])


@router.delete("/{course_id}", status_code=202, response_model=str)
async def course_delete(course_id: str, user_data: int= Depends(get_current_user)) :
    queryResult = db.child('student').child(course_id).get(user_data['idToken']).val()
    if not queryResult : 
        raise HTTPException(status_code=404, detail="Course not found")
    db.child('course').child(course_id).remove(token=user_data['idToken'])
    return "Student deleted"
