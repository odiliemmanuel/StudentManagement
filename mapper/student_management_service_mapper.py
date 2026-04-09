from models.course import Course
from models.role import Role
from models.user import User
from schemas.requests.create_new_course_request import CreateNewCourseRequest
from schemas.requests.create_user_request import CreateUserRequest
from schemas.responses.create_user_response import CreateUserResponse
from schemas.responses.create_new_course_response import CreateNewCourseResponse


class StudentManagementServiceMapper:


    @staticmethod
    def map_request_to_user(create_user_request: CreateUserRequest) -> User:


        return User(
            name=create_user_request.name,
            email=create_user_request.email,
            age=create_user_request.age,
            gender=create_user_request.gender,
            role=Role(create_user_request.role)
        )


    @staticmethod
    def map_user_to_create_user_response(user: User) -> CreateUserResponse:
          return CreateUserResponse(
              id=user.id,
              name=user.name,
              email=user.email,
              age=user.age,
              gender=user.gender,
              role=Role(user.role)
          )

    facilitator_id: str
    title: str
    description: str

    @staticmethod
    def map_create_new_course_request_to_course(create_new_course_request: CreateNewCourseRequest) -> Course:
        return Course(

            facilitator_id=create_new_course_request.facilitator_id,
            title=create_new_course_request.title,
            description=create_new_course_request.description

        )



    @staticmethod
    def map_course_to_create_new_course_response(course: Course) -> CreateNewCourseResponse:
        return CreateNewCourseResponse(
            course_id=course.course_id,
            message="Course successfully created",
            title=course.title,
            description=course.description,
            facilitator_id=course.facilitator_id
        )

    # @staticmethod
    # def map_enroll_student_