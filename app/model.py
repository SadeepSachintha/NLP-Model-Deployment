from transformers import pipeline
import logging

logger = logging.getLogger(__name__)

# Using a robust Sinhala sentiment analysis model from Hugging Face
MODEL_NAME = "keshan/sinhala-sentiment-analysis"
sentiment_pipeline = None

def load_model():
    global sentiment_pipeline
    if sentiment_pipeline is None:
        try:
            logger.info(f"Loading model {MODEL_NAME}...")
            sentiment_pipeline = pipeline("sentiment-analysis", model=MODEL_NAME)
            logger.info("Model loaded successfully.")
        except Exception as e:
            logger.error(f"Error loading model: {e}")
            raise e

def predict_sentiment(text: str):
    if not sentiment_pipeline:
        raise RuntimeError("Model pipeline is not initialized.")
    
    result = sentiment_pipeline(text)[0]
    return {
        "label": result["label"],
        "score": float(result["score"])
    }
