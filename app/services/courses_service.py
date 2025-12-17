# app/services/courses_service.py

# Simulación de base de datos en memoria
from fastapi import HTTPException

_courses = [
    {"id": 1, "name": "Python Básico"},
    {"id": 2, "name": "API REST con FastAPI"},
]


def get_courses():
    """
    Devuelve la lista de cursos disponibles.
    """
    return _courses


def add_course(name: str):
    """
    Agrega un nuevo curso a la lista y lo devuelve.
    """

    normalized_name = name.strip()

    if not normalized_name:
        raise HTTPException(
            status_code=400,
            detail="Course name is required"
        )

    for course in _courses:
        if course["name"].strip() == normalized_name:
            raise HTTPException(
                status_code=400,
                detail="Course already exists"
            )

    new_id = max(course["id"] for course in _courses) + 1

    new_course = {
        "id": new_id,
        "name": normalized_name,
    }

    _courses.append(new_course)
    return new_course







































# def add_course(name: str):
#     """
#     Agrega un nuevo curso a la lista y lo devuelve.
#     """
#     new_id = max(course["id"] for course in _courses) + 1

#     new_course = {
#         "id": new_id,
#         "name": name,
#     }

#     _courses.append(new_course)
#     return new_course



































# # app/services/courses_service.py

# # Simulación de base de datos en memoria
# _courses = [
#     {"id": 1, "name": "Python Básico"},
#     {"id": 2, "name": "API REST con FastAPI"},
# ]


# def get_courses():
#     """
#     Devuelve la lista de cursos disponibles.
#     """
#     return _courses


# def add_course(name: str):
#     """
#     Agrega un nuevo curso a la lista y lo devuelve.
#     """
#     new_id = max(course["id"] for course in _courses) + 1

#     new_course = {
#         "id": new_id,
#         "name": name,
#     }

#     _courses.append(new_course)
#     return new_course


































# # app/services/courses_service.py

# def get_courses():
#     """
#     Devuelve la lista de cursos disponibles.
#     Por ahora es información simulada (hardcoded).
#     """
#     return [
#         {"id": 1, "name": "Python Básico"},
#         {"id": 2, "name": "API REST con FastAPI"},
#     ]