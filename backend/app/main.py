from fastapi import FastAPI
from sqlalchemy import text
from app.db.session import engine
from app.api.v1.router import api_router

app = FastAPI(
    title="PrajaScan API",
    version="0.1.0",
    description="PrajaScan backend API (authorized scanning only).",
)

app.include_router(api_router, prefix="/api/v1")

@app.get("/health")
def health():
    return {"status": "ok", "service": "prajascan-api"}

@app.get("/db-check")
def db_check():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        return {"database": "connected", "result": result.scalar()}