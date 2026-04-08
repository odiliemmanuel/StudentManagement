from bson import ObjectId
from pymongo import MongoClient

from models.course import Course

client = MongoClient("mongodb://localhost:27017")
db = client["courses"]
course_collections = db["courses"]

class UserRepository:

    def save(self, course: Course):
        database = course.dict(by_alias=True)
        if database.get("_id"):
            course_collections.update_one({"_id": ObjectId(database["_id"])}, {"$set": database})
            return database

        value = course_collections.insert_one(database)
        return str(value.inserted_id)


    def find_by_id(self, course_id: str):
        database = course_collections.find_one({"_id": ObjectId(course_id)})
        if database:
            database["_id"] = str(database["_id"])
            return Course(**database)
        return None
