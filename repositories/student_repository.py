from bson import ObjectId
from pymongo import MongoClient

from models.user import User

client = MongoClient("mongodb://localhost:27017")
db = client["students"]
user_collections = db["students"]

class UserRepository:

    def save_student(self, user: User):
        data = user.dict(by_alias=True)
        if data.get("_id"):
            user_collections.update_one({"_id": ObjectId(data["_id"])}, {"$set": data})
            return data

        value = user_collections.insert_one(data)
        return str(value.inserted_id)

    def find_by_id(self, user_id: str):
        data = user_collections.find_one({"_id": ObjectId(user_id)})
        if data:
            data["_id"] = str(data["_id"])
            return User(**data)
        return None


