from litestar.testing import TestClient

from app.main import app
from app.services.irrigation import calculate_optimal_irrigation


def test_root():
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Litestar is working!"}


def test_calculate_optimal_irrigation():
    soil = {"moisture": 30}
    weather = {"forecast": "clear"}
    crop = {"type": "corn"}

    result = calculate_optimal_irrigation(soil, weather, crop)

    # проверим, что это число типа float
    assert isinstance(result, float)

    # и проверим ожидаемое поведение (заглушка возвращает 12.5)
    assert result == 12.5
