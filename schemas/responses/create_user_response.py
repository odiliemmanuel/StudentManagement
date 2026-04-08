from pydantic import BaseModel


class CreateUserResponse(BaseModel):
    id: str
    message: str
    name: str
    email_address: str
    age: int
    gender: str
    role: str