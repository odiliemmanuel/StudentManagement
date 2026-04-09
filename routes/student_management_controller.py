from fastapi import APIRouter

from exceptions.email_already_exist_exception import EmailAlreadyExistsException
from exceptions.messages import Messages
from schemas.requests.create_new_course_request import CreateNewCourseRequest
from schemas.requests.create_user_request import CreateUserRequest
from schemas.requests.enroll_student_in_course_request import EnrollStudentInCourseRequest
from schemas.responses.enroll_student_in_course_response import EnrollStudentInCourseResponse
from schemas.responses.create_new_course_response import CreateNewCourseResponse
from schemas.responses.create_user_response import CreateUserResponse
from services.student_management_service import StudentManagementService

router = APIRouter(prefix="/students", tags=["Students"])
services = StudentManagementService()




@router.post("/create-user", response_model=CreateUserResponse)
def create_user(request: CreateUserRequest) -> CreateUserResponse:
    try:
        return services.create_user(request)
    except Exception:
        raise EmailAlreadyExistsException(Messages.EMAIL_ALREADY_EXISTS_EXCEPTION)



@router.post("/facilitator/create-new-course", response_model=CreateNewCourseResponse)
def create_new_course(request: CreateNewCourseRequest) -> CreateNewCourseResponse:
    return services.create_new_course(request)



@router.post("/enroll-student-in-course", response_model=EnrollStudentInCourseResponse)
def enroll_student_in_a_course(request: EnrollStudentInCourseRequest) -> EnrollStudentInCourseResponse:
        return services.enroll_student_in_a_course(request)


@router.get("/student/view-course-title/{student_id}/{course_id}")
def view_course_title(student_id, course_id):
    return services.view_course_title(student_id, course_id)



@router.get("/student/view-course-description/{student_id}/{course_id}")
def view_course_description(student_id, course_id):
    return services.view_course_description(student_id, course_id)



@router.get("/view_facilitator-for-course/{course_id}")
def view_facilitator_for_course(course_id):
    return services.view_facilitator_for_course(course_id)