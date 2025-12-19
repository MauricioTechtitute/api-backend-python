# test/test_course_repositories.py
import pytest
from app.repositories.course_repository_sqlite import SqliteCourseRepository

# -------------------------------
# Test del repositorio SQLite
# -------------------------------
def test_sqlite_repo(tmp_path):
    db_path = tmp_path / "test_courses.db"
    repo = SqliteCourseRepository(str(db_path))
    
    # Crear un curso
    course_data = {"id": 1, "name": "Python Básico"}
    created_course = repo.create(course_data)
    assert created_course["name"] == "Python Básico"
    
    # Listar cursos
    courses = repo.list()
    assert len(courses) == 1
    assert courses[0]["name"] == "Python Básico"
    
    # Obtener curso
    course = repo.get(1)
    assert course["name"] == "Python Básico"
    
    # Actualizar curso
    repo.update(1, {"name": "Python Intermedio"})
    updated_course = repo.get(1)
    assert updated_course["name"] == "Python Intermedio"
    
    # Parchar curso
    repo.patch(1, {"name": "Python Avanzado"})
    patched_course = repo.get(1)
    assert patched_course["name"] == "Python Avanzado"
    
    # Eliminar curso
    repo.delete(1)
    assert repo.list() == []





































# # test/test_course_repositories.py
# import pytest
# from app.repositories.course_repository_in_memory import InMemoryCourseRepository
# from app.repositories.course_repository_sqlite import SqliteCourseRepository


# # -------------------------------
# # Test del repositorio en memoria
# # -------------------------------
# def test_in_memory_repo():
#     repo = InMemoryCourseRepository()
    
#     # Crear un curso
#     course_data = {"id": 1, "name": "Python Básico"}
#     repo.create(course_data)
    
#     # Listar cursos
#     courses = repo.list()
#     assert len(courses) == 1
#     assert courses[0]["name"] == "Python Básico"
    
#     # Obtener curso
#     course = repo.get(1)
#     assert course["name"] == "Python Básico"
    
#     # Actualizar curso
#     repo.update(1, {"name": "Python Intermedio"})
#     updated_course = repo.get(1)
#     assert updated_course["name"] == "Python Intermedio"
    
#     # Parchar curso
#     repo.patch(1, {"name": "Python Avanzado"})
#     patched_course = repo.get(1)
#     assert patched_course["name"] == "Python Avanzado"
    
#     # Eliminar curso
#     repo.delete(1)
#     assert repo.list() == []


# # -------------------------------
# # Test del repositorio SQLite
# # -------------------------------
# def test_sqlite_repo(tmp_path):
#     db_path = tmp_path / "test_courses.db"
#     repo = SqliteCourseRepository(str(db_path))
    
#     # Crear tabla de prueba
#     conn = repo._get_connection()
#     cursor = conn.cursor()
#     cursor.execute("""
#         CREATE TABLE courses (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             name TEXT NOT NULL
#         )
#     """)
#     conn.commit()
#     conn.close()
    
#     # Crear un curso
#     course_data = {"id": 1, "name": "Python Básico"}
#     repo.create(course_data)
    
#     # Listar cursos
#     courses = repo.list()
#     assert len(courses) == 1
#     assert courses[0]["name"] == "Python Básico"
    
#     # Obtener curso
#     course = repo.get(1)
#     assert course["name"] == "Python Básico"
    
#     # Actualizar curso
#     repo.update(1, {"name": "Python Intermedio"})
#     updated_course = repo.get(1)
#     assert updated_course["name"] == "Python Intermedio"
    
#     # Parchar curso
#     repo.patch(1, {"name": "Python Avanzado"})
#     patched_course = repo.get(1)
#     assert patched_course["name"] == "Python Avanzado"
    
#     # Eliminar curso
#     repo.delete(1)
#     assert repo.list() == []






























# # test/test_course_repositories.py
# import pytest
# from app.repositories.course_repository import CourseRepository
# from app.repositories.course_repository_sqlite import CourseRepositorySQLite
# # from app.repositories.course_repository_in_memory import InMemoryCourseRepository
# from app.repositories.course_repository_sqlite import SqliteCourseRepository  # ⚠ nombre corregido



# # -------------------------------
# # Test del repositorio en memoria
# # -------------------------------
# def test_in_memory_repo():
#     repo = InMemoryCourseRepository()
    
#     # Crear un curso
#     course_data = {"id": 1, "name": "Python Básico"}
#     repo.create(course_data)
    
#     # Listar cursos
#     courses = repo.list()
#     assert len(courses) == 1
#     assert courses[0]["name"] == "Python Básico"
    
#     # Obtener curso
#     course = repo.get(1)
#     assert course["name"] == "Python Básico"
    
#     # Actualizar curso
#     repo.update(1, {"name": "Python Intermedio"})
#     updated_course = repo.get(1)
#     assert updated_course["name"] == "Python Intermedio"
    
#     # Parchar curso
#     repo.patch(1, {"name": "Python Avanzado"})
#     patched_course = repo.get(1)
#     assert patched_course["name"] == "Python Avanzado"
    
#     # Eliminar curso
#     repo.delete(1)
#     assert repo.list() == []

# # -------------------------------
# # Test del repositorio SQLite
# # -------------------------------
# def test_sqlite_repo(tmp_path):
#     db_path = tmp_path / "test_courses.db"
#     repo = CourseRepositorySQLite(str(db_path))
    
#     # Crear un curso
#     course_data = {"id": 1, "name": "Python Básico"}
#     repo.create(course_data)
    
#     # Listar cursos
#     courses = repo.list()
#     assert len(courses) == 1
#     assert courses[0]["name"] == "Python Básico"
    
#     # Obtener curso
#     course = repo.get(1)
#     assert course["name"] == "Python Básico"
    
#     # Actualizar curso
#     repo.update(1, {"name": "Python Intermedio"})
#     updated_course = repo.get(1)
#     assert updated_course["name"] == "Python Intermedio"
    
#     # Parchar curso
#     repo.patch(1, {"name": "Python Avanzado"})
#     patched_course = repo.get(1)
#     assert patched_course["name"] == "Python Avanzado"
    
#     # Eliminar curso
#     repo.delete(1)
#     assert repo.list() == []





































# # test/test_course_repositories.py

# import pytest
# from app.repositories.course_repository import CourseRepository
# # from app.repositories.course_repository_sqlite import CourseRepositorySQLite
# from app.repositories.course_repository_sqlite import SqliteCourseRepository


# def test_in_memory_repo():
#     repo = CourseRepository()
    
#     # Agregar curso
#     course = {"id": 1, "name": "Python Básico"}
#     repo.add(course)
    
#     # Verificar curso agregado
#     all_courses = repo.list_all()
#     assert len(all_courses) == 1
#     assert all_courses[0]["name"] == "Python Básico"

# def test_sqlite_repo(tmp_path):
#     db_path = tmp_path / "test_courses.db"
#     repo = CourseRepositorySQLite(str(db_path))
    
#     # Agregar curso
#     course = {"id": 1, "name": "Python Avanzado"}
#     repo.add(course)
    
#     # Verificar curso agregado
#     all_courses = repo.list_all()
#     assert len(all_courses) == 1
#     assert all_courses[0]["name"] == "Python Avanzado"