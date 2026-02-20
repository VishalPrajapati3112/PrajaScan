from fastapi import FastAPI
from sqlalchemy import text
from app.db.session import engine

app = FastAPI(
    title="PrajaScan API",
    version="0.1.0",
)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/db-check")
def db_check():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        return {"database": "connected", "result": result.scalar()}
