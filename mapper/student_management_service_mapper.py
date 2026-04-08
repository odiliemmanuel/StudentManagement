from models.course import Course
from models.role import Role
from models.user import User
from schemas.requests.create_new_course_request import CreateNewCourseRequest
from schemas.requests.create_user_request import CreateUserRequest
from schemas.requests.enroll_student_in_course_request import EnrollStudentInCourseRequest
from schemas.responses.create_new_course_response import CreateNewCourseResponse
from schemas.responses.create_user_response import CreateUserResponse
from schemas.responses.enroll_student_in_course_response import EnrollStudentInCourseResponse


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
        return Course(
            user_id=create_new_course_request.user_id,
            title=create_new_course_request.title,
            description=create_new_course_request.description,
        )



    @staticmethod
    def map_course_to_create_new_course_response(course: Course) -> CreateNewCourseResponse:
        return CreateNewCourseResponse(
            course_id=course.id,
            message="Course created successfully",
            title=course.title,
            description=course.description,
            user_id=course.user_id,

        )



    @staticmethod
    def map_user_to_enroll_student_in_course_response(user : User) -> EnrollStudentInCourseResponse:
        return EnrollStudentInCourseResponse(
            student_id=user.id,
            course_id=[course.id for course in user.courses if course.id == user.course_id],
            facilitator_id=[course.user_id for course in user.courses],
            message="Course added successfully",
            title=[course.title for course in user.courses],
            description=[course.description for course in user.courses],

        )

