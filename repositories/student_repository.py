from bson import ObjectId
from pydantic import EmailStr
from pymongo import MongoClient

from models.user import User

client = MongoClient("mongodb://localhost:27017")
db = client["students"]
student_collections = db["students"]


class StudentRepository:


        def save(self, user: User):
            data = user.model_dump(by_alias=True)

            if not data.get("_id"):
                data.pop("_id", None)
                result = student_collections.insert_one(data)
                user.id = str(result.inserted_id)
                return user

            student_collections.update_one(
                {"_id": ObjectId(data["_id"])},
                {"$set": data}
            )
            return user



        def find_by_email(self, email: EmailStr) -> User | None:
            data = student_collections.find_one({"email_address": email})

            if data:
                data["_id"] = str(data["_id"])
                return User(**data)

            return None



        def find_by_id(self, user_id: str):
            data = student_collections.find_one({"_id": ObjectId(user_id)})

            if data:
                data["_id"] = str(data["_id"])
                return User(**data)

            return None



        def find_all(self):
            users = []

            for data in student_collections.find():
                data["_id"] = str(data["_id"])
                users.append(User(**data))

            return users