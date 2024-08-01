from pymongo import MongoClient
from app.config import Config

# print(f"Config.MONGO_DB_URI {Config.MONGO_DB_URI}")
client = MongoClient(Config.MONGO_DB_URI)

db = client["spbot"]


def get_collection(collection_name: str):
    return db[collection_name]
