from typing import List, Dict
from app.dependences.db.db import get_collection


def GetProducts() -> List[Dict]:
    collection = get_collection(collection_name="products")
    print(collection)
    return list(collection.find())
