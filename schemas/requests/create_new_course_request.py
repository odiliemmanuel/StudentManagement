from pydantic import BaseModel


class CreateNewCourseRequest(BaseModel):
    facilitator_id: str
    title: str
    description: str
