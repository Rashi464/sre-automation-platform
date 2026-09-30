from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_root():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["status"] == "running"


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_create_order():
    order = {
        "customer_name": "Test Customer",
        "product": "Laptop",
        "quantity": 1,
        "amount": 55000
    }

    response = client.post("/orders", json=order)

    assert response.status_code == 200

    data = response.json()

    assert data["customer_name"] == "Test Customer"
    assert data["product"] == "Laptop"
    assert data["status"] == "PLACED"