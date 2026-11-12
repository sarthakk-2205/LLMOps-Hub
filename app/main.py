from fastapi import FastAPI

app = FastAPI(
    title="LLMOps Hub",
    description="End-to-End LLM Monitoring and Evaluation Platform",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to LLMOps Hub",
        "status": "Running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "application": "LLMOps Hub"
    }