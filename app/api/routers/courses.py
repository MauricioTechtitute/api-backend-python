from fastapi import APIRouter, HTTPException
from app.api.schemas import Course, CourseCreate
# from app.services.courses_service import get_courses, add_course

from app.services.courses_service import get_courses, add_course, delete_course


router = APIRouter(
    prefix="/courses",
    tags=["courses"]
)


@router.get("/", response_model=list[Course])
def read_courses():
    return get_courses()


@router.post("/", response_model=Course, status_code=201)
def create_course(course: CourseCreate):

    return add_course(course.name)


@router.delete("/{course_id}", status_code=204)
def remove_course(course_id: int):
    try:
        delete_course(course_id)
    except ValueError:
        raise HTTPException(status_code=404, detail="Course not found")



























# from fastapi import APIRouter, HTTPException
# from app.api.schemas import Course, CourseCreate
# from app.services.courses_service import get_courses, add_course


# router = APIRouter(
#     prefix="/courses",
#     tags=["courses"]
# )


# @router.get("/", response_model=list[Course])
# def read_courses():
#     """
#     Obtiene la lista de cursos.
#     """
#     return get_courses()


# @router.post("/", response_model=Course, status_code=201)
# def create_course(course: CourseCreate):
#     """
#     Crea un nuevo curso.
#     """

#     if not course.name.strip():
#         raise HTTPException(
#             status_code=400,
#             detail="Course name is required"
#         )

#     return add_course(course.name)






























# from fastapi import APIRouter
# from app.api.schemas import Course, CourseCreate
# from app.services.courses_service import get_courses, add_course

# router = APIRouter(
#     prefix="/courses",
#     tags=["courses"]
# )


# @router.get("/", response_model=list[Course])
# def read_courses():
#     """
#     Obtiene la lista de cursos.
#     """
#     return get_courses()


# @router.post("/", response_model=Course, status_code=201)
# def create_course(course: CourseCreate):
#     """
#     Crea un nuevo curso.
#     """
#     return add_course(course.name)





































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