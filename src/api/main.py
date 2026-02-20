from fastapi import FastAPI
from src.config import settings
from src.schemas import ChatRequest, ChatResponse
from src.llm import LLMClient

app = FastAPI()
llm_client = LLMClient()


@app.get("/health")
async def health():
    return {"status": "ok"}

@app.post("/chat")
async def query_llm(message: ChatRequest):
    answer = await llm_client.query(message.question)
    return ChatResponse(answer=answer)
