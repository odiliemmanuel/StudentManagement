from pydantic import BaseModel


class CreateNewCourseResponse(BaseModel):
    course_id: str
    message: str
    title: str
    description: str
    facilitator_id: str