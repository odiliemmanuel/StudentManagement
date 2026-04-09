from fastapi import HTTPException

from exceptions.courseRoleMismatchException import CourseRoleMismatchException
from exceptions.email_already_exist_exception import EmailAlreadyExistsException
from exceptions.messages import Messages
from mapper.student_management_service_mapper import StudentManagementServiceMapper
from models.course import Course
from models.role import Role
from models.user import User
from repositories.course_repository import CourseRepository
from repositories.student_repository import StudentRepository
from schemas.requests.create_new_course_request import CreateNewCourseRequest
from schemas.requests.create_user_request import CreateUserRequest
from schemas.responses.create_new_course_response import CreateNewCourseResponse
from schemas.responses.create_user_response import CreateUserResponse


class StudentManagementService:

    def __init__(self):
        self.student_repository: StudentRepository = StudentRepository()
        self.course_repository: CourseRepository = CourseRepository()




    def create_user(self, request: CreateUserRequest) -> CreateUserResponse:
        if self.student_repository.find_by_email(request.email) is not None:
            raise EmailAlreadyExistsException(Messages.EMAIL_ALREADY_EXISTS_EXCEPTION)

        user :User = StudentManagementServiceMapper.map_request_to_user(request)

        self.student_repository.save(user)
        return StudentManagementServiceMapper.map_user_to_create_user_response(user)



    def create_new_course(self, request: CreateNewCourseRequest) -> CreateNewCourseResponse:
        user: User = self.student_repository.find_by_id(request.facilitator_id)

        if user.role != Role.FACILITATOR:
            raise HTTPException(status_code=403, detail="User is not a facilitator")

        course: Course = StudentManagementServiceMapper.map_create_new_course_request_to_course(request)
        course = self.course_repository.save(course)

        return StudentManagementServiceMapper.map_course_to_create_new_course_response(course)

























