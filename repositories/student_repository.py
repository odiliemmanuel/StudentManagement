from bson import ObjectId
from pymongo import MongoClient

from models.user import User

client = MongoClient("mongodb://localhost:27017")
db = client["students"]
user_collections = db["students"]


def save(user: User):
    data = user.model_dump()
    value = user_collections.insert_one(data)
    data.pop("_id", None)
    return str(value.inserted_id)




def find_by_id(user_id: str):
    data = user_collections.find_one({"_id": ObjectId(user_id)})
    if data:
        data["_id"] = str(data["_id"])
        return User(**data)
    return None


