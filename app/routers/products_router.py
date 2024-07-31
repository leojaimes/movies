from typing import List
from fastapi import APIRouter
from app.dependences.db.products import GetProducts

router = APIRouter()


@router.get("/products")
def getProducts():
    return GetProducts()
