from typing import List
from fastapi import APIRouter, HTTPException
from app.dependences.bson_to_json.generator import create_json_response
from app.dependences.utils import fibonnaci, userData
from app.models.user_models import UserBase
from app.schemas.user import user_entity, users_entity
from app.dependences.db.db import get_collection
from bson import ObjectId
from bson.json_util import dumps, loads
from bson import ObjectId
from fastapi.responses import JSONResponse


router = APIRouter()


@router.get("/users", tags=["users"])
def find_all_users():
    collection = get_collection("userwebs")
    users_db = list(collection.find({}, {"_id": 0}))
    return create_json_response(users_db)


@router.post("/users")
def create_user():
    return {}


@router.get("/users/{user_id}", tags=["users"])
def find_user_by_id(user_id):
    if not ObjectId.is_valid(user_id):
        raise HTTPException(status_code=400, detail="Invalid user ID format")

    collection = get_collection("userwebs")
    user_db = collection.find_one({"_id": ObjectId(user_id)})

    if user_db is None:
        raise HTTPException(status_code=404, detail="User not found")

    return dumps(user_db)


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
