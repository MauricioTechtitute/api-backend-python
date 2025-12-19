from typing import List, Optional
import sqlite3
from app.repositories.course_repository import CourseRepository

class SqliteCourseRepository(CourseRepository):
    """
    Implementación SQLite compatible con dicts como cursos.
    Soporta pasar la ruta de la DB para tests u otros entornos.
    """

    def __init__(self, db_path: Optional[str] = None):
        self.db_path = db_path
        # Crear tabla si no existe
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS courses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
        """)
        conn.commit()
        conn.close()

    def _get_connection(self):
        if self.db_path:
            return sqlite3.connect(self.db_path)
        else:
            from app.db.database import get_connection
            return get_connection()

    # ---------- Lecturas ----------
    def list(self) -> List[dict]:
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name FROM courses")
        rows = cursor.fetchall()
        conn.close()
        return [{"id": row[0], "name": row[1], "description": None} for row in rows]

    def get(self, course_id: int) -> Optional[dict]:
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name FROM courses WHERE id = ?", (course_id,))
        row = cursor.fetchone()
        conn.close()
        if row is None:
            return None
        return {"id": row[0], "name": row[1], "description": None}

    # ---------- Escrituras ----------
    def create(self, course: dict) -> dict:
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO courses (name) VALUES (?)", (course["name"],))
        course_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return {"id": course_id, "name": course["name"], "description": course.get("description")}

    def update(self, course_id: int, course: dict) -> dict:
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE courses SET name = ? WHERE id = ?", (course["name"], course_id))
        if cursor.rowcount == 0:
            conn.close()
            raise LookupError("Course not found")
        conn.commit()
        conn.close()
        return {"id": course_id, "name": course["name"], "description": course.get("description")}

    def patch(self, course_id: int, data: dict) -> dict:
        if not data:
            raise ValueError("Empty payload")

        fields = []
        values = []

        if "name" in data:
            fields.append("name = ?")
            values.append(data["name"])

        if not fields:
            raise ValueError("No valid fields to patch")

        values.append(course_id)

        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(f"UPDATE courses SET {', '.join(fields)} WHERE id = ?", values)

        if cursor.rowcount == 0:
            conn.close()
            raise LookupError("Course not found")

        conn.commit()

        cursor.execute("SELECT id, name FROM courses WHERE id = ?", (course_id,))
        row = cursor.fetchone()
        conn.close()

        return {"id": row[0], "name": row[1], "description": data.get("description")}

    def delete(self, course_id: int) -> None:
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM courses WHERE id = ?", (course_id,))
        if cursor.rowcount == 0:
            conn.close()
            raise LookupError("Course not found")
        conn.commit()
        conn.close()






























# from typing import List, Optional
# import sqlite3
# from app.db.database import get_connection
# from app.repositories.course_repository import CourseRepository

# class SqliteCourseRepository(CourseRepository):
#     """
#     Implementación SQLite compatible con dicts como cursos.
#     """

#     # ---------- Lecturas ----------
#     def list(self) -> List[dict]:
#         conn = get_connection()
#         cursor = conn.cursor()

#         cursor.execute("SELECT id, name FROM courses")
#         rows = cursor.fetchall()
#         conn.close()

#         return [{"id": row[0], "name": row[1], "description": None} for row in rows]

#     def get(self, course_id: int) -> Optional[dict]:
#         conn = get_connection()
#         cursor = conn.cursor()

#         cursor.execute("SELECT id, name FROM courses WHERE id = ?", (course_id,))
#         row = cursor.fetchone()
#         conn.close()

#         if row is None:
#             return None

#         return {"id": row[0], "name": row[1], "description": None}

#     # ---------- Escrituras ----------
#     def create(self, course: dict) -> dict:
#         conn = get_connection()
#         cursor = conn.cursor()

#         cursor.execute("INSERT INTO courses (name) VALUES (?)", (course["name"],))
#         course_id = cursor.lastrowid
#         conn.commit()
#         conn.close()

#         return {"id": course_id, "name": course["name"], "description": course.get("description")}

#     def update(self, course_id: int, course: dict) -> dict:
#         conn = get_connection()
#         cursor = conn.cursor()

#         cursor.execute("UPDATE courses SET name = ? WHERE id = ?", (course["name"], course_id))
#         if cursor.rowcount == 0:
#             conn.close()
#             raise LookupError("Course not found")

#         conn.commit()
#         conn.close()

#         return {"id": course_id, "name": course["name"], "description": course.get("description")}

#     def patch(self, course_id: int, data: dict) -> dict:
#         if not data:
#             raise ValueError("Empty payload")

#         fields = []
#         values = []

#         if "name" in data:
#             fields.append("name = ?")
#             values.append(data["name"])

#         if not fields:
#             raise ValueError("No valid fields to patch")

#         values.append(course_id)

#         conn = get_connection()
#         cursor = conn.cursor()
#         cursor.execute(f"UPDATE courses SET {', '.join(fields)} WHERE id = ?", values)

#         if cursor.rowcount == 0:
#             conn.close()
#             raise LookupError("Course not found")

#         conn.commit()

#         cursor.execute("SELECT id, name FROM courses WHERE id = ?", (course_id,))
#         row = cursor.fetchone()
#         conn.close()

#         return {"id": row[0], "name": row[1], "description": data.get("description")}

#     def delete(self, course_id: int) -> None:
#         conn = get_connection()
#         cursor = conn.cursor()

#         cursor.execute("DELETE FROM courses WHERE id = ?", (course_id,))
#         if cursor.rowcount == 0:
#             conn.close()
#             raise LookupError("Course not found")

#         conn.commit()
#         conn.close()







































# from typing import List, Optional

# from app.models.course import Course
# from app.repositories.course_repository import CourseRepository
# from app.db.database import get_connection


# class SqliteCourseRepository(CourseRepository):
#     """
#     Implementación SQLite que cumple estrictamente el contrato CourseRepository.

#     Notas:
#     - Lanza LookupError cuando un curso no existe (igual que memoria)
#     - Ignora campos no persistidos aún (ej: description) sin romper contrato
#     """

#     # ---------- Lecturas ----------

#     def list(self) -> List[Course]:
#         conn = get_connection()
#         cursor = conn.cursor()

#         cursor.execute("SELECT id, name FROM courses")
#         rows = cursor.fetchall()

#         conn.close()

#         return [Course(id=row[0], name=row[1], description=None) for row in rows]

#     def get(self, course_id: int) -> Optional[Course]:
#         conn = get_connection()
#         cursor = conn.cursor()

#         cursor.execute(
#             "SELECT id, name FROM courses WHERE id = ?",
#             (course_id,)
#         )
#         row = cursor.fetchone()
#         conn.close()

#         if row is None:
#             return None

#         return Course(id=row[0], name=row[1], description=None)

#     # ---------- Escrituras ----------

#     def create(self, course: Course) -> Course:
#         conn = get_connection()
#         cursor = conn.cursor()

#         cursor.execute(
#             "INSERT INTO courses (name) VALUES (?)",
#             (course.name,)
#         )

#         course_id = cursor.lastrowid
#         conn.commit()
#         conn.close()

#         return Course(
#             id=course_id,
#             name=course.name,
#             description=course.description,
#         )

#     def update(self, course_id: int, course: Course) -> Course:
#         conn = get_connection()
#         cursor = conn.cursor()

#         cursor.execute(
#             "UPDATE courses SET name = ? WHERE id = ?",
#             (course.name, course_id)
#         )

#         if cursor.rowcount == 0:
#             conn.close()
#             raise LookupError("Course not found")

#         conn.commit()
#         conn.close()

#         return Course(
#             id=course_id,
#             name=course.name,
#             description=course.description,
#         )

#     def patch(self, course_id: int, data: dict) -> Course:
#         if not data:
#             raise ValueError("Empty payload")

#         fields = []
#         values = []

#         if "name" in data:
#             fields.append("name = ?")
#             values.append(data["name"])

#         # description aún no se persiste en SQLite,
#         # pero se respeta el contrato sin romper flujo

#         if not fields:
#             raise ValueError("No valid fields to patch")

#         values.append(course_id)

#         conn = get_connection()
#         cursor = conn.cursor()

#         cursor.execute(
#             f"UPDATE courses SET {', '.join(fields)} WHERE id = ?",
#             values
#         )

#         if cursor.rowcount == 0:
#             conn.close()
#             raise LookupError("Course not found")

#         conn.commit()

#         cursor.execute(
#             "SELECT id, name FROM courses WHERE id = ?",
#             (course_id,)
#         )
#         row = cursor.fetchone()
#         conn.close()

#         return Course(
#             id=row[0],
#             name=row[1],
#             description=data.get("description"),
#         )

#     def delete(self, course_id: int) -> None:
#         conn = get_connection()
#         cursor = conn.cursor()

#         cursor.execute(
#             "DELETE FROM courses WHERE id = ?",
#             (course_id,)
#         )

#         if cursor.rowcount == 0:
#             conn.close()
#             raise LookupError("Course not found")

#         conn.commit()
#         conn.close()

































# from typing import List, Optional
# from app.models.course import Course
# from app.repositories.course_repository import CourseRepository
# from app.db.database import get_connection

# class SqliteCourseRepository(CourseRepository):

#     def get_all(self) -> List[Course]:
#         conn = get_connection()
#         cursor = conn.cursor()

#         cursor.execute("SELECT id, name FROM courses")
#         rows = cursor.fetchall()

#         conn.close()
#         return [Course(id=row[0], name=row[1]) for row in rows]

#     def get_by_id(self, course_id: int) -> Optional[Course]:
#         conn = get_connection()
#         cursor = conn.cursor()

#         cursor.execute(
#             "SELECT id, name FROM courses WHERE id = ?",
#             (course_id,)
#         )
#         row = cursor.fetchone()
#         conn.close()

#         if row is None:
#             return None

#         return Course(id=row[0], name=row[1])

#     def create(self, course: Course) -> Course:
#         conn = get_connection()
#         cursor = conn.cursor()

#         cursor.execute(
#             "INSERT INTO courses (name) VALUES (?)",
#             (course.name,)
#         )

#         course_id = cursor.lastrowid
#         conn.commit()
#         conn.close()

#         return Course(id=course_id, name=course.name)

#     def update(self, course_id: int, course: Course) -> Optional[Course]:
#         conn = get_connection()
#         cursor = conn.cursor()

#         cursor.execute(
#             "UPDATE courses SET name = ? WHERE id = ?",
#             (course.name, course_id)
#         )

#         if cursor.rowcount == 0:
#             conn.close()
#             return None

#         conn.commit()
#         conn.close()
#         return Course(id=course_id, name=course.name)

#     def delete(self, course_id: int) -> bool:
#         conn = get_connection()
#         cursor = conn.cursor()

#         cursor.execute(
#             "DELETE FROM courses WHERE id = ?",
#             (course_id,)
#         )

#         deleted = cursor.rowcount > 0
#         conn.commit()
#         conn.close()

#         return deleted