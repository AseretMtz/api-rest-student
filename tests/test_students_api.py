from fastapi.testclient import TestClient

import main


client = TestClient(main.app)


def setup_function() -> None:
    main._students.clear()
    main._next_id = 1


def test_health() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_full_crud_flow() -> None:
    payload = {"name": "Ana Perez", "age": 20, "email": "ana@example.com"}

    created = client.post("/students", json=payload)
    assert created.status_code == 201
    assert created.json()["id"] == 1

    listed = client.get("/students")
    assert listed.status_code == 200
    assert len(listed.json()) == 1

    found = client.get("/students/1")
    assert found.status_code == 200
    assert found.json()["name"] == "Ana Perez"

    updated = client.put("/students/1", json={"age": 21})
    assert updated.status_code == 200
    assert updated.json()["age"] == 21

    deleted = client.delete("/students/1")
    assert deleted.status_code == 204

    missing = client.get("/students/1")
    assert missing.status_code == 404


def test_email_validation_error() -> None:
    bad_payload = {"name": "Juan", "age": 19, "email": "no-es-email"}

    response = client.post("/students", json=bad_payload)

    assert response.status_code == 422
