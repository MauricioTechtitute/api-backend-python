from fastapi import APIRouter
from app.api.schemas import Course
from app.services.courses_service import get_courses

router = APIRouter(
    prefix="/courses",
    tags=["courses"]
)

@router.get("/", response_model=list[Course])
def read_courses():
    return get_courses()






# from fastapi import APIRouter

# router = APIRouter(
#     prefix="/courses",
#     tags=["courses"]
# )

# @router.get("/")
# def get_courses():
#     return [
#         {"id": 1, "name": "Python Básico"},
#         {"id": 2, "name": "API REST con FastAPI"}
#     ]