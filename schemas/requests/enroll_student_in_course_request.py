from pydantic import BaseModel


class EnrollStudentInCourseRequest(BaseModel):
    student_id: str
    course_id: str
