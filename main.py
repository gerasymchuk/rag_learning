from fastapi import FastAPI
from src.config import settings

app = FastAPI()


@app.get("/health")
async def root():
    print(settings.qdrant_url)
    return {"message": "Hello World"}

