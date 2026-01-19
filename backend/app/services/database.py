"""
Database service using Supabase
"""

from supabase import create_client, Client
from app.config import settings
from loguru import logger

# Initialize Supabase client
supabase: Client = create_client(
    settings.SUPABASE_URL,
    settings.SUPABASE_KEY
)

logger.info("Supabase client initialized")

async def init_database():
    """Initialize database tables if they don't exist"""
    try:
        # Tables are created via Supabase dashboard or SQL migrations
        # This function can be used for any initialization logic
        logger.info("Database initialized")
    except Exception as e:
        logger.error(f"Error initializing database: {e}")
        raise
