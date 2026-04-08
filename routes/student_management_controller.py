from fastapi import APIRouter
from schemas.responses.create_user_response import CreateUserResponse
from services.student_management_service import StudentManagementService
from repositories import student_repository, course_repository

router = APIRouter(prefix="/students", tags=["Students"])



services = StudentManagementService(student_repository, course_repository)

@router.post("/create-user", response_model=CreateUserResponse)


@router.post("/create-new-course", response_model=CreateNewCourseResponse)
