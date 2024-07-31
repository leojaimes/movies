from pymongo import MongoClient
from app.config import Config

# print(f"Config.MONGO_DB_URI {Config.MONGO_DB_URI}")
conn = MongoClient(Config.MONGO_DB_URI)
print(conn)
db = conn["teslo"]


def GetCollection(collection_name: str):
    return db[collection_name]
