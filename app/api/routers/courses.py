from fastapi import APIRouter
from app.api.schemas import Course

router = APIRouter(
    prefix="/courses",
    tags=["courses"]
)

@router.get("/", response_model=list[Course])
def get_courses():
    return [
        {"id": 1, "name": "Python Básico"},
        {"id": 2, "name": "API REST con FastAPI"}
    ]





























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