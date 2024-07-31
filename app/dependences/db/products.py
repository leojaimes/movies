from typing import List, Dict
from app.dependences.db.db import GetCollection


def GetProducts() -> List[Dict]:

    collection = GetCollection(collection_name="products")
    print(collection)
    return list(collection.find())
