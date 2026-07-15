from fastapi import FastAPI
from app.core.config import settings
from app.core.logging import configure_logging
import logging

configure_logging()

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
)

logger = logging.getLogger(__name__)
logger.info("Health endpoint called")

@app.get("/")
def root():
    return {"message": f"{settings.app_name} API"}

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
