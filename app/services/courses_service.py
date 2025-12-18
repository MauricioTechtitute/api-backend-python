from fastapi import HTTPException

# 🔴 CONTRATO EXISTENTE (NO SE ROMPE)
# _courses = [
#     {"id": 1, "name": "Python Básico"},
#     {"id": 2, "name": "API REST con FastAPI"},
# ]
_courses = [
    {"id": 1, "name": "Python Básico", "description": None},
    {"id": 2, "name": "API REST con FastAPI", "description": None},
]

class CourseRepository:
    def get_all(self):
        return _courses

    def add(self, name: str, description: str | None = None):
        normalized_name = name.strip()

        if not normalized_name:
            raise HTTPException(
                status_code=400,
                detail="Course name is required"
            )

        for course in _courses:
            if course["name"] == normalized_name:
                raise HTTPException(
                    status_code=400,
                    detail="Course already exists"
                )

        new_id = max(course["id"] for course in _courses) + 1

        new_course = {
            "id": new_id,
            "name": normalized_name,
            "description": description,
        }

        _courses.append(new_course)
        return new_course




# class CourseRepository:
#     def get_all(self):
#         return _courses

#     # def add(name: str, description: str | None = None):
#     def add_course(name: str, description: str | None = None):
#         normalized_name = name.strip()

#         if not normalized_name:
#             raise HTTPException(
#                 status_code=400,
#                 detail="Course name is required"
#             )

#         for course in _courses:
#             if course["name"] == normalized_name:
#                 raise HTTPException(
#                     status_code=400,
#                     detail="Course already exists"
#                 )

#         new_id = max(course["id"] for course in _courses) + 1

#         new_course = {
#             "id": new_id,
#             "name": normalized_name,
#             "description": description,
#         }

#         _courses.append(new_course)
#         # return new_course
#         return repo.add(name, description)


repo = CourseRepository()


def get_courses():
    return repo.get_all()


# def add_course(name: str, description: str | None = None):
# def add(self, name: str, description: str | None = None):
#     return repo.add(name, description)

def add_course(name: str, description: str | None = None):
    return repo.add(name, description)


def reset_courses():
    """
    Resetea el estado de cursos.
    Uso exclusivo para tests.
    """
    _courses.clear()
    # _courses.extend([
    #     {"id": 1, "name": "Python Básico", "description": None},
    #     {"id": 2, "name": "API REST con FastAPI", "description": None},
    # ])
    _courses.extend([
        {"id": 1, "name": "Python Básico", "description": None},
        {"id": 2, "name": "API REST con FastAPI", "description": None},
    ])



def update_course(course_id: int, name: str, description: str | None = None):
    if not name or not name.strip():
        raise ValueError("Course name is required")

    # verificar duplicado (otro curso)
    for course in _courses:
        if course["name"].lower() == name.lower() and course["id"] != course_id:
            raise ValueError("Course already exists")
    
    # for course in _courses:
    #     if course["name"].lower() == name.lower() and course["id"] != course_id:
    #         raise ValueError("Course already exists")

    # buscar curso
    for course in _courses:
        if course["id"] == course_id:
            course["name"] = name.strip()
            course["description"] = description
            return course

    raise KeyError("Course not found")


def delete_course(course_id: int):
    for course in _courses:
        if course["id"] == course_id:
            _courses.remove(course)
            return

    raise KeyError("Course not found")



# def patch_course(course_id: int, data: dict):
def patch_course(course_id: int, data: dict[str, str | None]):
    if not data:
        raise ValueError("Empty payload")

    course = next((c for c in _courses if c["id"] == course_id), None)
    if not course:
        raise LookupError("Course not found")

    if "name" in data:
        name = data["name"].strip()
        if not name:
            raise ValueError("Course name is required")

        if any(c["name"] == name and c["id"] != course_id for c in _courses):
            raise ValueError("Course already exists")

        course["name"] = name.strip()

    if "description" in data:
        description = data["description"]
        course["description"] = description

    return course


















# def patch_course(course_id: int, data: dict, description: str | None = None):
#     if not data:
#         raise ValueError("Empty payload")

#     course = next((c for c in _courses if c["id"] == course_id), None)
#     if not course:
#         raise LookupError("Course not found")

#     if "name" or "description" in data:
#         name = data["name"].strip()
#         description = data["description"].strip()

#         if not name or not description:
#             raise ValueError("Course name or description is required")

#         if any(c["name"] == name and c["description"] == description and c["id"] != course_id for c in _courses):
#             raise ValueError("Course already exists")

#         course["name"] = name
#         course["description"] = description

#     return course





































# from fastapi import HTTPException

# # 🔴 CONTRATO EXISTENTE (NO SE ROMPE)
# _courses = [
#     {"id": 1, "name": "Python Básico"},
#     {"id": 2, "name": "API REST con FastAPI"},
# ]


# class CourseRepository:
#     def get_all(self):
#         return _courses

#     def add(self, name: str):
#         normalized_name = name.strip()

#         if not normalized_name:
#             raise HTTPException(
#                 status_code=400,
#                 detail="Course name is required"
#             )

#         for course in _courses:
#             if course["name"] == normalized_name:
#                 raise HTTPException(
#                     status_code=400,
#                     detail="Course already exists"
#                 )

#         new_id = max(course["id"] for course in _courses) + 1

#         new_course = {
#             "id": new_id,
#             "name": normalized_name,
#         }

#         _courses.append(new_course)
#         return new_course


# repo = CourseRepository()


# def get_courses():
#     return repo.get_all()


# def add_course(name: str):
#     return repo.add(name)


# def reset_courses():
#     """
#     Resetea el estado de cursos.
#     Uso exclusivo para tests.
#     """
#     _courses.clear()
#     _courses.extend([
#         {"id": 1, "name": "Python Básico"},
#         {"id": 2, "name": "API REST con FastAPI"},
#     ])


# def update_course(course_id: int, name: str):
#     if not name or not name.strip():
#         raise ValueError("Course name is required")

#     # verificar duplicado (otro curso)
#     for course in _courses:
#         if course["name"].lower() == name.lower() and course["id"] != course_id:
#             raise ValueError("Course already exists")

#     # buscar curso
#     for course in _courses:
#         if course["id"] == course_id:
#             course["name"] = name
#             return course

#     raise KeyError("Course not found")


# def delete_course(course_id: int):
#     for course in _courses:
#         if course["id"] == course_id:
#             _courses.remove(course)
#             return

#     raise KeyError("Course not found")



# def patch_course(course_id: int, data: dict):
#     if not data:
#         raise ValueError("Empty payload")

#     course = next((c for c in _courses if c["id"] == course_id), None)
#     if not course:
#         raise LookupError("Course not found")

#     if "name" in data:
#         name = data["name"].strip()

#         if not name:
#             raise ValueError("Course name is required")

#         if any(c["name"] == name and c["id"] != course_id for c in _courses):
#             raise ValueError("Course already exists")

#         course["name"] = name

#     return course































# # app/services/courses_service.py

# # Simulación de base de datos en memoria
# from fastapi import HTTPException

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

#     normalized_name = name.strip()

#     if not normalized_name:
#         raise HTTPException(
#             status_code=400,
#             detail="Course name is required"
#         )

#     for course in _courses:
#         if course["name"].strip() == normalized_name:
#             raise HTTPException(
#                 status_code=400,
#                 detail="Course already exists"
#             )

#     new_id = max(course["id"] for course in _courses) + 1

#     new_course = {
#         "id": new_id,
#         "name": normalized_name,
#     }

#     _courses.append(new_course)
#     return new_course







































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