from pydantic import BaseModel


class ViewFacilitatorForCourseResponse(BaseModel):
    course_id: str
    facilitator_id: str
    facilitator_name: str
    facilitator_gender : str
