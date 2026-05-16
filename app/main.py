from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from app.model import predict_sentiment, load_model
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Sinhala Sentiment Analysis API",
    description="A robust REST API for predicting sentiment of Sinhala text.",
    version="1.0.0"
)

# Mount the static directory to serve CSS, JS, etc. if needed later, but mostly for the index.html
app.mount("/static", StaticFiles(directory="app/static"), name="static")

class SentimentRequest(BaseModel):
    text: str

class SentimentResponse(BaseModel):
    label: str
    score: float

@app.on_event("startup")
async def startup_event():
    """Load the model when the app starts."""
    try:
        load_model()
        logger.info("Model loaded successfully on startup")
    except Exception as e:
        logger.error(f"Failed to load model on startup: {e}")
        raise

@app.get("/", response_class=FileResponse)
def read_root():
    """Serve the frontend UI."""
    return "app/static/index.html"

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
