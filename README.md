---
title: NLP Model Deployment
emoji: 🚀
colorFrom: blue
colorTo: indigo
sdk: docker
pinned: false
---
# 🚀 Sinhala NLP Model Deployment (Cloud-Based API)

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue?style=for-the-badge)](https://huggingface.co/)
[![GitHub Actions](https://img.shields.io/badge/github%20actions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white)](https://github.com/features/actions)
[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/)

**🔴 [Live Demo on Hugging Face Spaces](https://huggingface.co/spaces/dwssp/NLP_Model)**

An automated, scalable, and production-ready REST API for Sinhala Sentiment Analysis. This project demonstrates the intersection of **AI/ML, Backend Engineering, and DevOps** by deploying a fine-tuned Hugging Face transformer model using FastAPI, Dockerized for portability, and automated via a GitHub Actions CI/CD pipeline.

---

## 🌟 Key Features

- **🧠 Native Sinhala NLP:** Utilizes `keshan/sinhala-sentiment-analysis` for accurate sentiment detection (Positive/Negative) in Sinhala text.
- **✨ Interactive Web UI:** Features a premium, dark-mode frontend built with modern glassmorphism design, allowing users to analyze text directly in their browser.
- **⚡ High-Performance Backend:** Built with **FastAPI** and **Uvicorn**, ensuring rapid response times, data validation via Pydantic, and automatic OpenAPI documentation.
- **🐳 Containerized Portability:** Fully Dockerized. The model is downloaded and cached during the Docker build stage for lightning-fast container startup.
- **⚙️ CI/CD Automation:** A robust **GitHub Actions** pipeline automatically tests the codebase and deploys the latest version to a free Hugging Face Docker Space upon merging to `main`.
- **☁️ Cloud-Native Architecture:** Designed to scale and run effortlessly on any cloud provider supporting Docker (currently deployed on Hugging Face Spaces).

---

## 🏗️ Architecture Flow

1. **Client** sends a POST request with Sinhala text to the API.
2. **FastAPI** validates the payload.
3. The **Transformers Pipeline** processes the text and infers sentiment.
4. The system returns a JSON response containing the sentiment label and confidence score.
5. All updates to the code trigger **GitHub Actions** -> Builds Docker Image -> Pushes to **HF Spaces**.

---

## 🚀 Getting Started Locally

### Prerequisites
- Python 3.10+
- Docker (Optional but recommended)

### Option 1: Run via Docker (Recommended)
```bash
# 1. Clone the repository
git clone https://github.com/yourusername/sinhala-nlp-deployment.git
cd "NLP + Deployment"

# 2. Build the Docker image (This will download the ML model)
docker build -t sinhala-nlp-api .

# 3. Run the container
docker run -p 7860:7860 sinhala-nlp-api
```
*The API is now running at `http://localhost:7860`*

### Option 2: Run via Python Virtual Environment
```bash
# 1. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Start the FastAPI server
uvicorn app.main:app --host 0.0.0.0 --port 7860 --reload
```

---

## 📖 API Documentation

Once the server is running, you can access the interactive Swagger UI at: `http://localhost:7860/docs`

### 1. Access the Web Interface
- **Endpoint:** `GET /`
- **Description:** Returns the beautiful, interactive HTML frontend where you can type Sinhala sentences and see real-time sentiment predictions.

### 2. Predict Sentiment
- **Endpoint:** `POST /predict`
- **Payload:**
  ```json
  {
    "text": "මෙය ඉතා හොඳ නිර්මාණයක්."
  }
  ```
- **Response:**
  ```json
  {
    "label": "LABEL_1",
    "score": 0.987654321
  }
  ```

---

## 🚢 CI/CD Deployment Guide

This project is pre-configured to deploy automatically to **Hugging Face Spaces**.

1. Create a free **Docker Space** on [Hugging Face](https://huggingface.co/spaces).
2. Navigate to your GitHub repository **Settings > Secrets and variables > Actions**.
3. Add the following repository secrets:
   - `HF_TOKEN`: Your Hugging Face Access Token.
   - `HF_USERNAME`: Your Hugging Face username.
   - `HF_SPACE_NAME`: The name of the space you created.
4. Push your code to the `main` branch. The GitHub Action will automatically run tests, build the Docker container, and deploy!

---
*Developed as a demonstration of scalable ML deployment pipelines.*
