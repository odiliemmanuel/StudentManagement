from fastapi import APIRouter
from pymongo.errors import DuplicateKeyError

from exceptions.email_already_exist_exception import EmailAlreadyExistsException
from exceptions.messages import Messages
from schemas.requests.create_user_request import CreateUserRequest
from schemas.responses.create_user_response import CreateUserResponse
from services.student_management_service import StudentManagementService

router = APIRouter(prefix="/students", tags=["Students"])

services = StudentManagementService()




@router.post("/create-user", response_model=CreateUserResponse)
def create_user(user: CreateUserRequest) -> CreateUserResponse:
    try:
        return services.create_user(user)
    except DuplicateKeyError:
        raise EmailAlreadyExistsException(Messages.EMAIL_ALREADY_EXISTS_EXCEPTION)



