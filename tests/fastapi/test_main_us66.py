from fastapi.testclient import TestClient
from py_fastapi.us66.main_us66 import app

def test_create_user_valid():
    client = TestClient(app)
    payload = {"name": "Alice", "email": "alice@example.com"}
    response = client.post("/user", json=payload)
    assert response.status_code == 200
    assert response.json()["success"] is True
    assert response.json()["data"] == payload

def test_create_user_invalid():
    client = TestClient(app)
    payload = {"name": "Alice", "email": "not-an-email"}
    response = client.post("/user", json=payload)
    assert response.status_code == 422
    assert "detail" in response.json()

    # Missing name
    payload = {"email": "alice@example.com"}
    response = client.post("/user", json=payload)
    assert response.status_code == 422
    assert "detail" in response.json()
