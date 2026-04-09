from pydantic import BaseModel, EmailStr


class CreateUserResponse(BaseModel):
    id: str
    name: str
    email: EmailStr
    age: int
    gender: str
    role: str