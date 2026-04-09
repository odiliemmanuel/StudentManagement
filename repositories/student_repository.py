from bson import ObjectId
from pydantic import EmailStr
from models.role import Role
from models.user import User
from database import student_collections



class StudentRepository:


        def save(self, user: User):
            data = user.model_dump(by_alias=True)
            print("Saving")

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
            data = student_collections.find_one({"email": email})

            if data:
                data["_id"] = str(data["_id"])
                return User(**data)

            return None

        def find_by_id(self, user_id: str):
            data = student_collections.find_one({"_id": ObjectId(user_id)})

            if data:
                data["_id"] = str(data["_id"])
                data["role"] = Role(data["role"])  # ✅ CRITICAL FIX
                return User(**data)

            return None



        def find_all(self):
            users = []

            for data in student_collections.find():
                data["_id"] = str(data["_id"])
                users.append(User(**data))

            return users