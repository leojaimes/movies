from typing import List
from fastapi import APIRouter
from app.dependences.utils import fibonnaci, userData
from app.models.user_models import UserBase
from app.schemas.user import user_entity, users_entity
from app.dependences.db.db import get_collection

router = APIRouter()


@router.get("/users")
def find_all_users():
    collection = get_collection("userwebs")
    users_db = list(collection.find({}, {"_id": 0}))
    return users_entity(users_db)


@router.post("/users")
def create_user():
    return {}


@router.get("/users/{userId}", tags=["users"])
def find_user_by_id(userId):
    return {"username": f"user{userId}"}


@router.put("/users/{userId}")
def update_user():
    return {}


@router.delete("/users/{userId}")
def delete_user():
    return {}


#
#
#
#
@router.get("/users-random", response_model=List[UserBase], tags=["users"])
def generate_random_users(n: int = 5):
    return list(userData(n))


#
#
#
#


#
#
#
#
@router.get("/fibonnaci", tags=["users"])
def generate_fibonnacci_users():
    numElements = 6
    users = [
        {"user": f"user {i}", "value": value}
        for i, value in enumerate(fibonnaci(numElements))
    ]
    return users
