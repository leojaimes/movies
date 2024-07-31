from pymongo import MongoClient
from app.config import Config

client = MongoClient(Config.MONGO_DB_URI)
db = client["teslo"]


def GetCollection(collection_name: str):
    return db[collection_name]
