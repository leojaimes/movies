from typing import List, Dict
from app.dependences.db.db import GetCollection


def GetProducts() -> List[Dict]:
    collection = GetCollection(collection_name="products")
    return list(collection.find())
