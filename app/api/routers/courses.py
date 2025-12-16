from fastapi import APIRouter

router = APIRouter(
    prefix="/courses",
    tags=["courses"]
)

@router.get("/")
def get_courses():
    return [
        {"id": 1, "name": "Python Básico"},
        {"id": 2, "name": "API REST con FastAPI"}
    ]