from fastapi import FastAPI

app = FastAPI(
    title="AI Content OS",
    version="0.1.0"
)

@app.get("/")
def root():
    return {"message": "AI Content OS API"}

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }