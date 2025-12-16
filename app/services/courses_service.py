# app/services/courses_service.py

def get_courses():
    """
    Devuelve la lista de cursos disponibles.
    Por ahora es información simulada (hardcoded).
    """
    return [
        {"id": 1, "name": "Python Básico"},
        {"id": 2, "name": "API REST con FastAPI"},
    ]