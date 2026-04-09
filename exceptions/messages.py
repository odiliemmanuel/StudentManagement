from pydantic import EmailStr


class Messages:

    COURSE_ROLE_MISMATCH_EXCEPTION = "Student cannot create course"
    INVALID_COURSE_ID_EXCEPTION = "Course with given id does not exist"
    INVALID_STUDENT_ID_EXCEPTION = "Student with given id does not exist"
    INVALID_EMAIL_EXCEPTION = "Email address entered is not valid"
    EMAIL_ALREADY_EXISTS_EXCEPTION = "Email address already exists"
    INVALID_ID_ENTRY_EXCEPTION = "Cannot find id"
    INVALID_ROLE_EXCEPTION = "Invalid role"
