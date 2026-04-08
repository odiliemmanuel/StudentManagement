from pydantic import BaseModel


class CreateUserRequest(BaseModel):
    name: str
    email_address: str
    age: int
    gender: str
    role: str