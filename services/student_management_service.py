from exceptions.CourseRoleMismatchException import CourseRoleMismatchException
from exceptions.messages import Messages
from mapper.student_management_service_mapper import StudentManagementServiceMapper
from models.role import Role
from models.user import User
from schemas.requests.create_new_course_request import CreateNewCourseRequest
from schemas.requests.create_user_request import CreateUserRequest
from schemas.responses.create_user_response import CreateUserResponse


class StudentManagementService:

    def __init__(self, user_repository, course_repository):
        self.user_repository = user_repository
        self.course_repository = course_repository





    def create_user(self, create_user_request: CreateUserRequest) -> CreateUserResponse:

        user = StudentManagementServiceMapper.map_request_to_user(create_user_request)
        inserted_id = self.user_repository.save(user)
        user.id = inserted_id

        return StudentManagementServiceMapper.map_user_to_response(user)



    def create_new_course(self, create_new_course_request: CreateNewCourseRequest):
        user : User = self.user_repository.find_by_id(create_new_course_request.user_id)

        if user.role == Role.FACILITATOR:
            course = StudentManagementServiceMapper.map_create_new_course_request_to_course(create_new_course_request)
            inserted_id = self.course_repository.save(course)
            course.id = inserted_id

            return StudentManagementServiceMapper.map_course_to_create_new_course_response(course)

        else:
            raise CourseRoleMismatchException(Messages.COURSE_ROLE_MISMATCH_EXCEPTION)
