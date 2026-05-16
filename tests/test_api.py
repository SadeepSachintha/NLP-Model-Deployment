from fastapi.testclient import TestClient
from app.main import app
import pytest

@pytest.fixture(scope="module")
def client():
    with TestClient(app) as c:
        yield c

def test_read_root(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "Welcome" in response.json()["message"]

def test_predict_sentiment_positive(client):
    # "This is a very good creation." in Sinhala
    response = client.post("/predict", json={"text": "මෙය ඉතා හොඳ නිර්මාණයක්."}) 
    assert response.status_code == 200
    assert "label" in response.json()
    assert "score" in response.json()

def test_predict_sentiment_empty(client):
    response = client.post("/predict", json={"text": ""})
    assert response.status_code == 400
