from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')
    qdrant_url: str
    ollama_url: str
    llm_model: str = "llama3.1:latest"

settings = Settings()