from app.main import app
from litestar.testing import TestClient


def test_root():
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Litestar is working!"}
