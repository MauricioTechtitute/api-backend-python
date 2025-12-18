from fastapi import APIRouter, HTTPException
from app.api.schemas import Course, CourseCreate
# from app.services.courses_service import get_courses, add_course

from app.services.courses_service import (
    get_courses,
    add_course,
    delete_course,
    update_course,
    patch_course,
)

router = APIRouter(
    prefix="/courses",
    tags=["courses"]
)


@router.get("/", response_model=list[Course])
def read_courses():
    return get_courses()


@router.post("/", response_model=Course, status_code=201)
def create_course(course: CourseCreate):

    # return add_course(course.name)
    return add_course(course.name, course.description)




@router.put("/{course_id}", response_model=Course)
def update_course_endpoint(course_id: int, course: CourseCreate):
    try:
        # return update_course(course_id, course.name)
        return update_course(course_id, course.name, course.description)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    # except KeyError as e:
    #     raise HTTPException(status_code=404, detail=str(e))
    except KeyError:
        raise HTTPException(status_code=404, detail="Course not found")



@router.patch("/{course_id}", response_model=Course)
def patch_course_endpoint(course_id: int, payload: dict):
# def patch_course_endpoint(course_id: int, payload: CoursePatch):
    try:
        # return patch_course(course_id,  payload.model_dump(exclude_unset=True))
        return patch_course(course_id, payload)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except LookupError as e:
        raise HTTPException(status_code=404, detail=str(e))























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