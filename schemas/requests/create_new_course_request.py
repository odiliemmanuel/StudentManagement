from pydantic import BaseModel


class CreateNewCourseRequest(BaseModel):
    user_id: str
    title: str
    description: str
