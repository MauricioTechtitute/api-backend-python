from typing import List, Optional
from app.models.course import Course
from app.repositories.course_repository import CourseRepository
from app.db.database import get_connection

class SqliteCourseRepository(CourseRepository):

    def get_all(self) -> List[Course]:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT id, name FROM courses")
        rows = cursor.fetchall()

        conn.close()
        return [Course(id=row[0], name=row[1]) for row in rows]

    def get_by_id(self, course_id: int) -> Optional[Course]:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT id, name FROM courses WHERE id = ?",
            (course_id,)
        )
        row = cursor.fetchone()
        conn.close()

        if row is None:
            return None

        return Course(id=row[0], name=row[1])

    def create(self, course: Course) -> Course:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO courses (name) VALUES (?)",
            (course.name,)
        )

        course_id = cursor.lastrowid
        conn.commit()
        conn.close()

        return Course(id=course_id, name=course.name)

    def update(self, course_id: int, course: Course) -> Optional[Course]:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "UPDATE courses SET name = ? WHERE id = ?",
            (course.name, course_id)
        )

        if cursor.rowcount == 0:
            conn.close()
            return None

        conn.commit()
        conn.close()
        return Course(id=course_id, name=course.name)

    def delete(self, course_id: int) -> bool:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM courses WHERE id = ?",
            (course_id,)
        )

        deleted = cursor.rowcount > 0
        conn.commit()
        conn.close()

        return deleted