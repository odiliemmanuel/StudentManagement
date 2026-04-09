from pymongo import MongoClient


client = MongoClient("mongodb://localhost:27017")


students_db= client["students"]
student_collections = students_db["students"]
course_db = client["courses"]
course_collections = course_db["courses"]
