from fastapi.testclient import TestClient
from app.main import app
import pytest
from unittest.mock import patch

@pytest.fixture(scope="module")
def client():
    # Mock the model loading and prediction during tests
    with patch('app.main.load_model'):
        with patch('app.main.predict_sentiment') as mock_predict:
            mock_predict.return_value = {"label": "POSITIVE", "score": 0.95}
            with TestClient(app) as c:
                yield c

def test_read_root(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
    assert "Sinhala Sentiment Analysis API" in response.text

def test_predict_sentiment_positive(client):
    # "This is a very good creation." in Sinhala
    response = client.post("/predict", json={"text": "මෙය ඉතා හොඳ නිර්මාණයක්."}) 
    assert response.status_code == 200
    assert "label" in response.json()
    assert "score" in response.json()

def test_predict_sentiment_empty(client):
    response = client.post("/predict", json={"text": ""})
    assert response.status_code == 400
