from fastapi import FastAPI

from config import settings

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
)

@app.get("/")
def root():
    return {"message": f"{settings.app_name} API"}

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
