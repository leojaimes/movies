from typing import List
from fastapi import APIRouter
from app.dependences.utils import fibonnaci, userData
from app.models.user_models import UserBase
 

router = APIRouter()

@router.get("/users",  response_model=List[UserBase], tags=['users'])
def getUsers(n:int = 5 ):
    return  list(userData(n))

@router.get("/users/{userId}", tags=['users'])
def getUserById(userId):
    return {"username": f"user{userId}"}

@router.get("/fibonnaci", tags=['users'])
def getFibonacciUsers():
    numElements = 6
    users = [
        {"user": f"user {i}", "value": value}
        for i, value in enumerate(fibonnaci(numElements))
    ]
    return users

