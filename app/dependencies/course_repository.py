from app.core.settings import settings
from app.repositories.course_repository import CourseRepository
from app.repositories.course_repository_memory import InMemoryCourseRepository
from app.repositories.course_repository_sqlite import SqliteCourseRepository

def get_course_repository() -> CourseRepository:
    if settings.COURSE_REPOSITORY == "sqlite":
        return SqliteCourseRepository()
    return InMemoryCourseRepository()