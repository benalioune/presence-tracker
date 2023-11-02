import firebase_admin
from firebase_admin import credentials
import pyrebase
import json

from configs.firebase_config import firebaseConfig

from dotenv import dotenv_values






# import des crédentiels
if not firebase_admin._apps:
    cred = credentials.Certificate("configs/sessiontracker-6fe1e-firebase-adminsdk-dpt5s-d09a504710.json")
    firebase_admin.initialize_app(cred)


firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()
authStudent = firebase.auth()