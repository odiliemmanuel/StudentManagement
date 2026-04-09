from fastapi import APIRouter
from pymongo.errors import DuplicateKeyError

from exceptions.courseRoleMismatchException import CourseRoleMismatchException
from exceptions.email_already_exist_exception import EmailAlreadyExistsException
from exceptions.messages import Messages
from schemas.requests.create_new_course_request import CreateNewCourseRequest
from schemas.requests.create_user_request import CreateUserRequest
from schemas.responses.create_new_course_response import CreateNewCourseResponse
from schemas.responses.create_user_response import CreateUserResponse
from services.student_management_service import StudentManagementService

router = APIRouter(prefix="/students", tags=["Students"])

services = StudentManagementService()




@router.post("/create-user", response_model=CreateUserResponse)
def create_user(user: CreateUserRequest) -> CreateUserResponse:
    try:
        return services.create_user(user)
    except Exception:
        raise EmailAlreadyExistsException(Messages.EMAIL_ALREADY_EXISTS_EXCEPTION)




@router.post("/facilitator/create-new-course", response_model=CreateNewCourseResponse)
def create_new_course(course: CreateNewCourseRequest) -> CreateNewCourseResponse:

    return services.create_new_course(course)
