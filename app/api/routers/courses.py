from fastapi import APIRouter
from app.api.schemas import Course, CourseCreate
from app.services.courses_service import get_courses, add_course

router = APIRouter(
    prefix="/courses",
    tags=["courses"]
)


@router.get("/", response_model=list[Course])
def read_courses():
    """
    Obtiene la lista de cursos.
    """
    return get_courses()


@router.post("/", response_model=Course, status_code=201)
def create_course(course: CourseCreate):
    """
    Crea un nuevo curso.
    """
    return add_course(course.name)





































# from fastapi import APIRouter
# from app.api.schemas import Course
# from app.services.courses_service import get_courses

# router = APIRouter(
#     prefix="/courses",
#     tags=["courses"]
# )

# @router.get("/", response_model=list[Course])#Aparentemente sin el slash no necesitaría escribir /courses/ sino con /courses bastaría: @router.get("", response_model=list[Course])
# def read_courses():
#     return get_courses()







































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