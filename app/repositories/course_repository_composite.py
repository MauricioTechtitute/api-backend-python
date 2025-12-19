from typing import List, Optional

from app.models.course import Course
from app.repositories.course_repository import CourseRepository


class CompositeCourseRepository(CourseRepository):
    """
    Repositorio compuesto que delega operaciones a dos repositorios concretos.

    Estrategia:
    - Escrituras (create, update, delete): se ejecutan en ambos repositorios
    - Lecturas (list, get): se delegan a un repositorio canónico
    """

    def __init__(
        self,
        primary_repository: CourseRepository,
        secondary_repository: CourseRepository,
    ):
        self._primary = primary_repository
        self._secondary = secondary_repository

    # ---------- Lecturas ----------

    def list(self) -> List[Course]:
        return self._primary.list()

    def get(self, course_id: int) -> Optional[Course]:
        return self._primary.get(course_id)

    # ---------- Escrituras ----------

    def create(self, course: Course) -> Course:
        created = self._primary.create(course)
        self._secondary.create(course)
        return created

    def update(self, course_id: int, course: Course) -> Course:
        updated = self._primary.update(course_id, course)
        self._secondary.update(course_id, course)
        return updated

    def delete(self, course_id: int) -> None:
        self._primary.delete(course_id)
        self._secondary.delete(course_id)