from routes import  student_management_controller
from fastapi import FastAPI

app = FastAPI(
    title="Student API",
    description="A restful API to handle student creation,assignment,etc.",
    version="1.0",
)


app.include_router(student_management_controller.router)



