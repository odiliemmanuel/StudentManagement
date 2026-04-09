from bson import ObjectId
from models.course import Course
from models.role import Role
from database import course_collections


class CourseRepository:

    def save(self, course: Course):
        data = course.model_dump(by_alias=True)

        if not data.get("_id"):
            data.pop("_id", None)
            result = course_collections.insert_one(data)
            course.course_id = str(result.inserted_id)
            return course

        course_collections.update_one(
            {"_id": ObjectId(data["_id"])},
            {"$set": data}
        )
        return course


    def find_by_id(self, user_id: str):
        data = course_collections.find_one({"_id": ObjectId(user_id)})

        if data:
            data["_id"] = str(data["_id"])
            return Course(**data)

        return None






    def find_by_title(self, title: str):
        data = course_collections.find_one({"title": title})

        if data:
            data["_id"] = str(data["_id"])
            return Course(**data)

        return None


    def find_all(self):
        users = []

        for data in course_collections.find():
            data["_id"] = str(data["_id"])
            users.append(Course(**data))

        return users