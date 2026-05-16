from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.model import predict_sentiment
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Sinhala Sentiment Analysis API",
    description="A robust REST API for predicting sentiment of Sinhala text.",
    version="1.0.0"
)

class SentimentRequest(BaseModel):
    text: str

class SentimentResponse(BaseModel):
    label: str
    score: float

@app.get("/")
def read_root():
    return {"message": "Welcome to the Sinhala Sentiment Analysis API. Use POST /predict to analyze text."}

@app.post("/predict", response_model=SentimentResponse)
def predict(request: SentimentRequest):
    if not request.text or len(request.text.strip()) == 0:
        raise HTTPException(status_code=400, detail="Text cannot be empty.")
    
    try:
        result = predict_sentiment(request.text)
        return result
    except Exception as e:
        logger.error(f"Prediction error: {e}")
        raise HTTPException(status_code=500, detail="Internal server error during prediction.")
