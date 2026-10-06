from fastapi import FastAPI
from datetime import datetime
import random

app = FastAPI(
    title="Srujan's FastAPI Demo",
    description="A demo API to learn FastAPI, Docker and Kubernetes",
    version="1.0.0"
)

quotes = [
    "Code. Build. Deploy.",
    "Containers make life easier.",
    "Automation beats repetition.",
    "Learn Terraform, Build Cloud.",
    "Every expert was once a beginner."
]

@app.get("/", tags=["Home"])
def home():
    return {
        "message": "🚀 Welcome to FastAPI!",
        "author": "Srujan",
        "server_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

@app.get("/health", tags=["Monitoring"])
def health():
    return {
        "status": "healthy ✅",
        "uptime": "running"
    }

@app.get("/quote", tags=["Fun"])
def quote():
    return {
        "quote": random.choice(quotes)
    }

@app.get("/about", tags=["Info"])
def about():
    return {
        "application": "FastAPI Demo",
        "framework": "FastAPI",
        "containerized": True,
        "kubernetes_ready": True
    }

@app.get("/stats", tags=["Metrics"])
def stats():
    return {
        "users": 125,
        "deployments": 12,
        "containers_running": 3
    }