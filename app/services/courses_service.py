from app.api.schemas import Course

def get_all_courses() -> list[Course]:
    """
    Devuelve la lista de cursos.
    Por ahora es una lista fija (simula una base de datos).
    """
    """
    Devuelve la lista de cursos.
    Por ahora es una lista fija.
    Más adelante aquí irá la base de datos.
    """    
    return [
        Course(id=1, name="Python Básico"),
        Course(id=2, name="API REST con FastAPI"),
    ]