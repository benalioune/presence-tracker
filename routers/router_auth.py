from fastapi import APIRouter, Depends, HTTPException
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from classes.schemas_dto import User

from fastapi.security import OAuth2PasswordBearer

from classes.schemas_dto import User
from firebase_admin import auth, credentials
from database.firebase import authStudent

from typing import Annotated

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='auth/login')
def get_current_user(provided_token: str = Depends(oauth2_scheme)):
    decoded_token = auth.verify_id_token(provided_token)
    decoded_token['idToken'] = provided_token
    return decoded_token

router  =  APIRouter(
    
    tags=["Auth"],
    prefix='/auth'
    
)
#signup endPoint
@router.post('signup', status_code=201)
async def signup(request: Request):
    # request de l'email et du password
   req = await request.json()
   email = req['email']
   password = req['password']
   
   # si on reçoit pas d'email et de mdp 
   if email is None or password is None:
       # on retourne un message d'erreur 
       return HTTPException(detail={'message': 'Error! Missing Email or Password'}, status_code=400)
   # Sinon on stock les champs les variables email et mdp dans notre liste de user
   try:
       user = auth.create_user(
           email=email,
           password=password
       )
       # et on retourne le message avec l'id de l'utilisateur créer et status 200 
       return JSONResponse(content={'message': f'Successfully created user {user.uid}'}, status_code=200)    
   except:
       return HTTPException(detail={'message': 'Error Creating User'}, status_code=400)


#login endPoint
@router.post('/login')
async def create_swagger_token(user_credentials: OAuth2PasswordRequestForm = Depends()):
    try :       
        user = authStudent.sign_in_with_email_and_password(email=user_credentials.username, password=user_credentials.password)
        token = user['idToken']
        print(token)
        return {
            'access_token': token,
            'token_type': 'bearer'
        }
    except :
        raise HTTPException(status_code=401, detail='Invalid credentials')



 
#protect route to get personal data 
@router.get('/me')
def secure_endpoint(user_data: int = Depends(get_current_user)):
    return user_data
