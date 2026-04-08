from models.role import Role
from models.user import User
from schemas.requests.create_user_request import CreateUserRequest
from schemas.responses.create_user_response import CreateUserResponse


class StudentManagementServiceMapper:


    @staticmethod
    def map_request_to_user(create_user_request: CreateUserRequest) -> User:
        return User(
            name=create_user_request.name,
            email_address=create_user_request.email_address,
            age=create_user_request.age,
            gender=create_user_request.gender,
            role=Role(create_user_request.role)
        )


    @staticmethod
    def map_user_to_create_user_response(user: User) -> CreateUserResponse:
      return CreateUserResponse(
          name=user.name,
          email_address=user.email_address,
          age=user.age,
          gender=user.gender,

      )

