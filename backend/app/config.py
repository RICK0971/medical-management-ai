"""
Application configuration
"""

from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    # Project
    PROJECT_NAME: str = "Medical Management AI"
    ENVIRONMENT: str = "development"
    DEBUG: bool = True
    API_V1_PREFIX: str = "/api/v1"
    
    # Database
    DATABASE_URL: str = ""
    
    # Supabase
    SUPABASE_URL: str = ""
    SUPABASE_KEY: str = ""
    SUPABASE_SERVICE_KEY: str = ""
    
    # LLM
    GROQ_API_KEY: str = ""
    OPENROUTER_API_KEY: str = ""
    
    # Auth
    SECRET_KEY: str = "your-secret-key-change-this-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # CORS
    ALLOWED_ORIGINS: List[str] = [
        "http://localhost:3000",
        "http://localhost:3001",
    ]
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()
