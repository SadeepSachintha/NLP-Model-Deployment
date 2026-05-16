from transformers import pipeline
import logging

logger = logging.getLogger(__name__)

# Using a robust Sinhala sentiment analysis model from Hugging Face
MODEL_NAME = "keshan/sinhala-sentiment-analysis"

try:
    logger.info(f"Loading model {MODEL_NAME}...")
    sentiment_pipeline = pipeline("sentiment-analysis", model=MODEL_NAME)
    logger.info("Model loaded successfully.")
except Exception as e:
    logger.error(f"Error loading model: {e}")
    sentiment_pipeline = None

def predict_sentiment(text: str):
    if not sentiment_pipeline:
        raise RuntimeError("Model pipeline is not initialized.")
    
    result = sentiment_pipeline(text)[0]
    return {
        "label": result["label"],
        "score": float(result["score"])
    }
