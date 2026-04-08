from mapper.student_management_service_mapper import StudentManagementServiceMapper
from schemas.requests.create_user_request import CreateUserRequest
from schemas.responses.create_user_response import CreateUserResponse


class StudentManagementService:

    def __init__(self, user_repository):
        self.repository = user_repository



    def create_user(self, create_user_request: CreateUserRequest) -> CreateUserResponse:

        user = StudentManagementServiceMapper.map_request_to_user(create_user_request)

        inserted_id = self.repository.save(user)
        user.id = inserted_id

        return StudentManagementServiceMapper.map_user_to_response(user)



    def create_new_course(self,):
        pass
