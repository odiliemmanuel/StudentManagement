from typing import Optional
from pydantic import BaseModel, Field
from models.course import Course
from models.role import Role


class User(BaseModel):
    id: Optional[str] = Field(default=None, alias="_id")
    name: str
    email_address: str
    age: int
    gender: str
    role: Role
    courses: list[Course]
