from pydantic import BaseModel


class EnrollStudentInCourseResponse(BaseModel):
    student_id: str
    course_id: str
    facilitator_id: str
    message : str
    title : str
    description : str