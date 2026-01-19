"""
AI Chat API routes
"""

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from loguru import logger

from app.services.auth_service import get_current_user
from app.agents.medical_agent import run_medical_agent

router = APIRouter()

class ChatMessage(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str

@router.post("/", response_model=ChatResponse)
async def chat(
    chat_message: ChatMessage,
    current_user: dict = Depends(get_current_user)
):
    """Chat with the medical AI agent"""
    try:
        response = await run_medical_agent(
            user_id=current_user['id'],
            user_name=current_user['name'],
            message=chat_message.message
        )
        
        return ChatResponse(response=response)
        
    except Exception as e:
        logger.error(f"Chat error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to process chat message"
        )
