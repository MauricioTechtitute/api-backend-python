from fastapi import HTTPException

# 🔴 CONTRATO EXISTENTE (NO SE ROMPE)
_courses = [
    {"id": 1, "name": "Python Básico", "description": None},
    {"id": 2, "name": "API REST con FastAPI", "description": None},
]


class CourseRepository:
    def get_all(self):
        return _courses

    def add(self, name: str, description: str | None = None) -> dict:
        normalized_name = name.strip()

        if not normalized_name:
            raise HTTPException(
                status_code=400,
                detail="Course name is required"
            )

        if self._name_exists(normalized_name):
            raise HTTPException(
                status_code=400,
                detail="Course already exists"
            )

        new_id = max(course["id"] for course in _courses) + 1

        course = {
            "id": new_id,
            "name": normalized_name,
            "description": description,
        }

        _courses.append(course)
        return course

    def update(self, course_id: int, name: str, description: str | None) -> dict:
        normalized_name = name.strip()

        if not normalized_name:
            raise HTTPException(
                status_code=400,
                detail="Course name is required"
            )

        course = self._get_or_404(course_id)

        if self._name_exists(normalized_name, exclude_id=course_id):
            raise HTTPException(
                status_code=400,
                detail="Course already exists"
            )

        course["name"] = normalized_name
        course["description"] = description
        return course

    def patch(self, course_id: int, payload: dict) -> dict:
        if not payload:
            raise HTTPException(
                status_code=400,
                detail="Empty payload"
            )

        course = self._get_or_404(course_id)

        if "name" in payload:
            name = payload["name"].strip()

            if not name:
                raise HTTPException(
                    status_code=400,
                    detail="Course name is required"
                )

            if self._name_exists(name, exclude_id=course_id):
                raise HTTPException(
                    status_code=400,
                    detail="Course already exists"
                )

            course["name"] = name

        if "description" in payload:
            course["description"] = payload["description"]

        return course

    def delete(self, course_id: int) -> None:
        course = self._get_or_404(course_id)
        _courses.remove(course)

    def reset(self):
        _courses.clear()
        _courses.extend([
            {"id": 1, "name": "Python Básico", "description": None},
            {"id": 2, "name": "API REST con FastAPI", "description": None},
        ])

    # 🔒 Helpers privados

    def _get_or_404(self, course_id: int) -> dict:
        for course in _courses:
            if course["id"] == course_id:
                return course
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    def _name_exists(self, name: str, exclude_id: int | None = None) -> bool:
        for course in _courses:
            if exclude_id is not None and course["id"] == exclude_id:
                continue
            if course["name"].lower() == name.lower():
                return True
        return False


# 🔹 API pública usada por routers y tests
repo = CourseRepository()
# from app.dependencies.course_repository import get_course_repository

# repo = get_course_repository()


def get_courses():
    return repo.get_all()

def add_course(name: str, description: str | None = None):
    return repo.add(name, description)

def update_course(course_id: int, name: str, description: str | None):
    return repo.update(course_id, name, description)

def patch_course(course_id: int, payload: dict):
    return repo.patch(course_id, payload)

def delete_course(course_id: int):
    repo.delete(course_id)

def reset_courses():
    repo.reset()































# from fastapi import HTTPException

# # 🔴 CONTRATO EXISTENTE (NO SE ROMPE)
# # _courses = [
# #     {"id": 1, "name": "Python Básico"},
# #     {"id": 2, "name": "API REST con FastAPI"},
# # ]
# _courses = [
#     {"id": 1, "name": "Python Básico", "description": None},
#     {"id": 2, "name": "API REST con FastAPI", "description": None},
# ]

# class CourseRepository:
#     def get_all(self):
#         return _courses

#     def add(self, name: str, description: str | None = None):
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
#         return new_course




# # class CourseRepository:
# #     def get_all(self):
# #         return _courses

# #     # def add(name: str, description: str | None = None):
# #     def add_course(name: str, description: str | None = None):
# #         normalized_name = name.strip()

# #         if not normalized_name:
# #             raise HTTPException(
# #                 status_code=400,
# #                 detail="Course name is required"
# #             )

# #         for course in _courses:
# #             if course["name"] == normalized_name:
# #                 raise HTTPException(
# #                     status_code=400,
# #                     detail="Course already exists"
# #                 )

# #         new_id = max(course["id"] for course in _courses) + 1

# #         new_course = {
# #             "id": new_id,
# #             "name": normalized_name,
# #             "description": description,
# #         }

# #         _courses.append(new_course)
# #         # return new_course
# #         return repo.add(name, description)


# repo = CourseRepository()


# def get_courses():
#     return repo.get_all()


# # def add_course(name: str, description: str | None = None):
# # def add(self, name: str, description: str | None = None):
# #     return repo.add(name, description)

# # def add_course(name: str, description: str | None = None):
# #     return repo.add(name, description)
# # def add_course(name: str, description: str | None = None) -> dict:
# #     # global _next_id
# #     new_id = max(course["id"] for course in _courses) + 1

# #     course = {
# #     "id": new_id,
# #     "name": normalized_name,
# #     "description": description,
# # }
    

# #     if not name or not name.strip():
# #         raise ValueError("Course name cannot be empty")

# #     normalized_name = _normalize_name(name)

# #     if _course_name_exists(normalized_name):
# #         raise ValueError("Course with this name already exists")

# #     course = {
# #         "id": _next_id,
# #         "name": normalized_name,
# #         "description": description,
# #     }

# #     _courses.append(course)
# #     _next_id += 1

# #     return course

# def add_course(name: str, description: str | None = None) -> dict:
#     if not name or not name.strip():
#         raise ValueError("Course name cannot be empty")

#     normalized_name = _normalize_name(name)

#     if _course_name_exists(normalized_name):
#         raise ValueError("Course with this name already exists")

#     new_id = max(course["id"] for course in _courses) + 1

#     course = {
#         "id": new_id,
#         "name": normalized_name,
#         "description": description,
#     }

#     _courses.append(course)
#     return course


# def reset_courses():
#     """
#     Resetea el estado de cursos.
#     Uso exclusivo para tests.
#     """
#     _courses.clear()
#     # _courses.extend([
#     #     {"id": 1, "name": "Python Básico", "description": None},
#     #     {"id": 2, "name": "API REST con FastAPI", "description": None},
#     # ])
#     _courses.extend([
#         {"id": 1, "name": "Python Básico", "description": None},
#         {"id": 2, "name": "API REST con FastAPI", "description": None},
#     ])



# # def update_course(course_id: int, name: str, description: str | None = None):
# #     if not name or not name.strip():
# #         raise ValueError("Course name is required")

# #     # verificar duplicado (otro curso)
# #     for course in _courses:
# #         if course["name"].lower() == name.lower() and course["id"] != course_id:
# #             raise ValueError("Course already exists")
    
# #     # for course in _courses:
# #     #     if course["name"].lower() == name.lower() and course["id"] != course_id:
# #     #         raise ValueError("Course already exists")

# #     # buscar curso
# #     for course in _courses:
# #         if course["id"] == course_id:
# #             course["name"] = name.strip()
# #             course["description"] = description
# #             return course

# #     raise KeyError("Course not found")


# # def delete_course(course_id: int):
# #     for course in _courses:
# #         if course["id"] == course_id:
# #             _courses.remove(course)
# #             return

# #     raise KeyError("Course not found")
# def update_course(course_id: int, name: str, description: str | None) -> dict:
#     if not name or not name.strip():
#         raise ValueError("Course name cannot be empty")

#     normalized_name = _normalize_name(name)

#     course = _get_course_or_raise(course_id)

#     if _course_name_exists(normalized_name, exclude_id=course_id):
#         raise ValueError("Course with this name already exists")

#     course["name"] = normalized_name
#     course["description"] = description

#     return course




# # def patch_course(course_id: int, data: dict):
# def patch_course(course_id: int, payload: dict) -> dict:
#     if not payload:
#         raise ValueError("Empty payload")

#     course = _get_course_or_raise(course_id)

#     if "name" in payload:
#         name = payload["name"]
#         if not name or not name.strip():
#             raise ValueError("Course name cannot be empty")

#         normalized_name = _normalize_name(name)

#         if _course_name_exists(normalized_name, exclude_id=course_id):
#             raise ValueError("Course with this name already exists")

#         course["name"] = normalized_name

#     if "description" in payload:
#         course["description"] = payload["description"]

#     return course


# def delete_course(course_id: int) -> None:
#     course = _get_course_or_raise(course_id)
#     _courses.remove(course)


# # def patch_course(course_id: int, data: dict[str, str | None]):
# #     if not data:
# #         raise ValueError("Empty payload")

# #     course = next((c for c in _courses if c["id"] == course_id), None)
# #     if not course:
# #         raise LookupError("Course not found")

# #     if "name" in data:
# #         name = data["name"].strip()
# #         if not name:
# #             raise ValueError("Course name is required")

# #         if any(c["name"] == name and c["id"] != course_id for c in _courses):
# #             raise ValueError("Course already exists")

# #         course["name"] = name.strip()

# #     if "description" in data:
# #         description = data["description"]
# #         course["description"] = description

# #     return course



# def _normalize_name(name: str) -> str:
#     return name.strip()


# def _course_name_exists(name: str, exclude_id: int | None = None) -> bool:
#     for course in _courses:
#         if exclude_id is not None and course["id"] == exclude_id:
#             continue
#         if course["name"].lower() == name.lower():
#             return True
#     return False


# def _get_course_or_raise(course_id: int) -> dict:
#     for course in _courses:
#         if course["id"] == course_id:
#             return course
#     raise KeyError("Course not found")



























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