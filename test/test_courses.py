from fastapi.testclient import TestClient
from app.main import app


import pytest
from app.services import courses_service


client = TestClient(app)

# 🔽 🔽 🔽 AQUÍ VA EL FIXTURE 🔽 🔽 🔽
@pytest.fixture(autouse=True)
def reset_courses():
    courses_service.reset_courses()

    # courses_service._courses.clear()
    # courses_service._courses.extend([
    #     {"id": 1, "name": "Python Básico"},
    #     {"id": 2, "name": "API REST con FastAPI"},
    # ])
# 🔼 🔼 🔼 FIN DEL FIXTURE 🔼 🔼 🔼

def test_get_courses_returns_list():
    response = client.get("/courses/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)



def test_get_courses_returns_valid_course_structure():
    response = client.get("/courses/")
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, list)

    if len(data) > 0:
        course = data[0]
        assert "id" in course
        assert "name" in course



def test_create_course_returns_created_course():
    payload = {
        "name": "Curso de prueba"
    }

    response = client.post("/courses/", json=payload)

    assert response.status_code == 201

    data = response.json()
    assert "id" in data
    assert data["name"] == payload["name"]



def test_create_course_with_empty_name_returns_400():
    payload = {
            "name": "   "
        }

    response = client.post("/courses/", json=payload)

    assert response.status_code == 400
    assert response.json()["detail"] == "Course name is required"



def test_create_course_with_duplicate_name_returns_400():
    payload = {"name": "Curso duplicado"}

    response1 = client.post("/courses/", json=payload)
    assert response1.status_code == 201

    response2 = client.post("/courses/", json=payload)
    assert response2.status_code == 400
    assert response2.json()["detail"] == "Course already exists"


def test_delete_course_returns_204():
    # crear curso
    payload = {"name": "Curso a eliminar"}
    create_response = client.post("/courses/", json=payload)
    assert create_response.status_code == 201

    course_id = create_response.json()["id"]

    # eliminar curso
    delete_response = client.delete(f"/courses/{course_id}")
    assert delete_response.status_code == 204


def test_delete_nonexistent_course_returns_404():
    response = client.delete("/courses/9999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Course not found"
