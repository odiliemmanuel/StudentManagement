from pydantic import BaseModel


class CreateUserResponse(BaseModel):
    id: str
    name: str
    email_address: str
    age: int
    gender: str
