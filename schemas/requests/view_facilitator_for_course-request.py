from pydantic import BaseModel


class ViewFacilitatorForCourseRequest(BaseModel):
    course_id: int