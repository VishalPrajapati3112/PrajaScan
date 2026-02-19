from fastapi import FastAPI

app = FastAPI(
    title="PrajaScan API",
    version="0.1.0",
    description="PrajaScan backend API (authorized scanning only).",
)

@app.get("/health")
def health():
    return {
        "status": "ok",
        "service": "prajascan-api",
    }
