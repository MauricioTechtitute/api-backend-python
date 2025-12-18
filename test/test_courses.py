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




def test_update_course_returns_updated_course():
    # crear curso
    payload = {"name": "Curso original"}
    create_response = client.post("/courses/", json=payload)
    assert create_response.status_code == 201

    course_id = create_response.json()["id"]

    # actualizar curso
    update_payload = {"name": "Curso actualizado"}
    update_response = client.put(f"/courses/{course_id}", json=update_payload)

    assert update_response.status_code == 200

    data = update_response.json()
    assert data["id"] == course_id
    assert data["name"] == "Curso actualizado"


def test_update_course_with_empty_name_returns_400():
    payload = {"name": "Curso válido"}
    create_response = client.post("/courses/", json=payload)
    assert create_response.status_code == 201

    course_id = create_response.json()["id"]

    update_payload = {"name": "   "}
    update_response = client.put(f"/courses/{course_id}", json=update_payload)

    assert update_response.status_code == 400
    assert update_response.json()["detail"] == "Course name is required"



def test_update_nonexistent_course_returns_404():
    update_payload = {"name": "Curso inexistente"}

    response = client.put("/courses/9999", json=update_payload)

    assert response.status_code == 404
    assert response.json()["detail"] == "Course not found"



def test_update_course_with_duplicate_name_returns_400():
    response1 = client.post("/courses/", json={"name": "Curso A"})
    response2 = client.post("/courses/", json={"name": "Curso B"})

    assert response1.status_code == 201
    assert response2.status_code == 201

    course_b_id = response2.json()["id"]

    update_payload = {"name": "Curso A"}
    update_response = client.put(f"/courses/{course_b_id}", json=update_payload)

    assert update_response.status_code == 400
    assert update_response.json()["detail"] == "Course already exists"




def test_patch_course_updates_name():
    response = client.post("/courses/", json={"name": "Curso Original"})
    course_id = response.json()["id"]

    patch_response = client.patch(
        f"/courses/{course_id}",
        json={"name": "Curso Actualizado"}
    )

    assert patch_response.status_code == 200
    assert patch_response.json()["name"] == "Curso Actualizado"


def test_patch_course_with_empty_name_returns_400():
    response = client.post("/courses/", json={"name": "Curso Válido"})
    course_id = response.json()["id"]

    patch_response = client.patch(
        f"/courses/{course_id}",
        json={"name": "   "}
    )

    assert patch_response.status_code == 400
    assert patch_response.json()["detail"] == "Course name is required"


def test_patch_course_with_duplicate_name_returns_400():
    client.post("/courses/", json={"name": "Curso A"})
    response_b = client.post("/courses/", json={"name": "Curso B"})
    course_b_id = response_b.json()["id"]

    patch_response = client.patch(
        f"/courses/{course_b_id}",
        json={"name": "Curso A"}
    )

    assert patch_response.status_code == 400
    assert patch_response.json()["detail"] == "Course already exists"


def test_patch_nonexistent_course_returns_404():
    patch_response = client.patch(
        "/courses/9999",
        json={"name": "Curso Inexistente"}
    )

    assert patch_response.status_code == 404
    assert patch_response.json()["detail"] == "Course not found"


def test_patch_course_with_empty_payload_returns_400():
    response = client.post("/courses/", json={"name": "Curso Válido"})
    course_id = response.json()["id"]

    patch_response = client.patch(
        f"/courses/{course_id}",
        json={}
    )

    assert patch_response.status_code == 400
