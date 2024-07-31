from typing import List
from fastapi import APIRouter
from app.dependences.db.products import GetProducts
import pandas as pd

router = APIRouter()


@router.get("/products")
def getProducts():
    # print(GetProducts().count)
    # df = pd.DataFrame(GetProducts())
    # print(df)
    # products_json = df.to_dict(orient="records")

    df = pd.DataFrame(GetProducts())
    return {}
