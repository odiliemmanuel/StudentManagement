from fastapi import HTTPException

from exceptions.courseRoleMismatchException import CourseRoleMismatchException
from exceptions.email_already_exist_exception import EmailAlreadyExistsException
from exceptions.invalid_course_id_exception import InvalidCourseIdException
from exceptions.invalid_id_entry_exception import InvalidIdEntryException
from exceptions.invalid_role_exception import InvalidRoleException
from exceptions.invalid_student_id_exception import InvalidStudentIdException
from exceptions.messages import Messages
from mapper.student_management_service_mapper import StudentManagementServiceMapper
from models.course import Course
from models.role import Role
from models.user import User
from repositories.course_repository import CourseRepository
from repositories.student_repository import StudentRepository
from schemas.requests.create_new_course_request import CreateNewCourseRequest
from schemas.requests.create_user_request import CreateUserRequest
from schemas.requests.enroll_student_in_course_request import EnrollStudentInCourseRequest
from schemas.responses.enroll_student_in_course_response import EnrollStudentInCourseResponse
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




    def enroll_student_in_a_course(self, request: EnrollStudentInCourseRequest) -> EnrollStudentInCourseResponse:
        student = self.student_repository.find_by_id(request.student_id)
        course = self.course_repository.find_by_id(request.course_id)

        if student.id == request.student_id and course.course_id == request.course_id:
            if student.role != Role.FACILITATOR:
                return StudentManagementServiceMapper.map_enroll_student_in_course_response_to_user(course, student)

            else:
                raise CourseRoleMismatchException(Messages.COURSE_ROLE_MISMATCH_EXCEPTION)

        else:
            raise InvalidStudentIdException(Messages.INVALID_STUDENT_ID_EXCEPTION) or InvalidCourseIdException(Messages.INVALID_COURSE_ID_EXCEPTION)



    def view_course_title(self, student_id, course_id) -> str:
        student = self.student_repository.find_by_id(student_id)
        course = self.course_repository.find_by_id(course_id)
        if course.course_id == course_id and student.role != Role.FACILITATOR and student.id == student_id:
            return course.title
        else:
             raise InvalidCourseIdException(Messages.INVALID_COURSE_ID_EXCEPTION)



    def view_course_description(self,student_id, course_id) -> str:
        student = self.student_repository.find_by_id(student_id)
        course = self.course_repository.find_by_id(course_id)
        if course.course_id == course_id and student.role != Role.FACILITATOR and student.id == student_id:
            return course.description
        else:
            raise InvalidCourseIdException(Messages.INVALID_COURSE_ID_EXCEPTION)




    def view_facilitator_for_course(self ,course_id) -> User:
        course = self.course_repository.find_by_id(course_id)
        facilitator = self.student_repository.find_by_id(course.facilitator_id)
        return facilitator



    def update_user_name(self, user_id: str, name) -> User:
        user = self.student_repository.find_by_id(user_id)
        user.name=name
        self.student_repository.save(user)
        return user


