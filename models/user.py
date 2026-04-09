from typing import Optional
from pydantic import BaseModel, Field, EmailStr

from models.role import Role


class User(BaseModel):
    id: Optional[str] = Field(default=None, alias="_id")
    name: str
    email: EmailStr
    age: int
    gender: str
    role: Role
    is_enrolled: bool

