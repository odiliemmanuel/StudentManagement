from typing import Optional

from pydantic import BaseModel, Field


class Student(BaseModel):
    id : Optional[str] = Field(default=None, alias="_id")
    name: str
    email_address: str
    age: int
    gender: str