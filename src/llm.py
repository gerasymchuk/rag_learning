from langchain_ollama import ChatOllama
from fastapi import HTTPException

from src.config import settings

class LLMClient:
    def __init__(self):
        self.llm = ChatOllama(model=settings.llm_model, base_url=settings.ollama_url, temperature=0)

    async def query(self, question: str) -> str:
        try:
            response = await self.llm.ainvoke(question)
            return response.content
        except Exception as e:
            raise HTTPException(status_code=502, detail=f"LLM error: {e}")