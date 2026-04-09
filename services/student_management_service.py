from fastapi import HTTPException

from exceptions.email_already_exist_exception import EmailAlreadyExistsException
from exceptions.messages import Messages
from mapper.student_management_service_mapper import StudentManagementServiceMapper
from models.user import User
from repositories.student_repository import StudentRepository
from schemas.requests.create_user_request import CreateUserRequest
from schemas.responses.create_user_response import CreateUserResponse


class StudentManagementService:

    def __init__(self):
        self.student_repository: StudentRepository = StudentRepository()


    def create_user(self, request: CreateUserRequest) -> CreateUserResponse:
        if self.student_repository.find_by_email(request.email) is not None:
            raise EmailAlreadyExistsException(Messages.EMAIL_ALREADY_EXISTS_EXCEPTION)

        user :User = StudentManagementServiceMapper.map_request_to_user(request)

        self.student_repository.save(user)
        return StudentManagementServiceMapper.map_user_to_create_user_response(user)

























