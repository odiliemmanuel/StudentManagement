from typing import Optional

from pydantic import BaseModel, Field


class Course(BaseModel):
    id: Optional[str] = Field(default=None, alias='_id')
    facilitator_id: str
    title: str
    description: str