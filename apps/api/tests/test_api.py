from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_translate_stub() -> None:
    response = client.post(
        "/v1/translate",
        json={
            "text": "i ni",
            "source_language": "susu",
            "target_language": "en",
        },
    )
    assert response.status_code == 200
    assert response.json()["translation"] == "hello"
