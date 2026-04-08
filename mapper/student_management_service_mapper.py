from models.role import Role
from models.user import User
from schemas.requests.create_new_course_request import CreateNewCourseRequest
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
            role =Role(create_user_request.role.upper()),

        )



    @staticmethod
    def map_user_to_response(user: User) -> CreateUserResponse:
        return CreateUserResponse(
            id=user.id,
            name=user.name,
            email_address=user.email_address,
            age=user.age,
            gender=user.gender,
            role=str(user.role),
            message ="User created successfully"

        )


    @staticmethod
    def map_create_new_course_request_to_course(create_new_course_request: CreateNewCourseRequest) -> Course:




            # user_id: str
            # title: str
            # description: str