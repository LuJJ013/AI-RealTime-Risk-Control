from fastapi import FastAPI, HTTPException
from sqlalchemy.exc import SQLAlchemyError

from database.connection import check_database_connection

app = FastAPI()


@app.get("/")
def root():
    return {
        "message": "AI Big Data Platform",
        "status": "running"
    }


@app.get("/hello")
def hello():
    return {
        "message": "Hello FastAPI"
    }


@app.get("/health")
def health():
    """Report that the API process is running."""
    return {"status": "ok"}


@app.get("/health/db")
def database_health():
    """Check database connectivity without exposing connection details."""
    try:
        check_database_connection()
    except SQLAlchemyError:
        raise HTTPException(
            status_code=503,
            detail={"status": "unavailable", "database": "disconnected"},
        )
    return {"status": "ok", "database": "connected"}
