# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /code

# Copy the requirements file into the container
COPY ./requirements.txt /code/requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r /code/requirements.txt

# Create a non-root user for security (Hugging Face Spaces requirement)
RUN useradd -m -u 1000 user
USER user
ENV HOME=/home/user \
    PATH=/home/user/.local/bin:$PATH

WORKDIR $HOME/app

# Copy the current directory contents into the container
COPY --chown=user . $HOME/app

# Pre-download the Hugging Face model during the build stage
# This saves time and bandwidth during container startup
RUN --mount=type=secret,id=HF_TOKEN,mode=0444,required=true \
    python -c "import os; from transformers import pipeline; token = open('/run/secrets/HF_TOKEN').read().strip(); pipeline('sentiment-analysis', model='keshan/sinhala-sentiment-analysis', token=token)"

# Make port 7860 available to the world outside this container
EXPOSE 7860

# Run main.py when the container launches
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "7860"]
