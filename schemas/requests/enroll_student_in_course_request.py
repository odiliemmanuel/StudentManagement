from pydantic import BaseModel


class EnrollStudentInCourseRequest(BaseModel):
    student_id: str
    course_id: str
    course_title: str
    course_description: str