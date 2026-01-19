"""
Medical AI Agent using Pydantic AI
"""

from pydantic_ai import Agent
from loguru import logger

from app.config import settings
from .tools import (
    MedicalContext,
    get_medications,
    add_medication,
    get_appointments,
    schedule_appointment,
    log_health_metric,
    get_health_trends
)

# System prompt for the medical agent
SYSTEM_PROMPT = """You are a helpful medical management assistant named MediBot.

Your role is to help users:
- Track and manage their medications
- Schedule and manage doctor appointments
- Log and analyze health metrics (blood pressure, blood sugar, weight, etc.)
- Answer general health questions
- Provide medication reminders

IMPORTANT GUIDELINES:
1. Always include medical disclaimers when giving health advice
2. Suggest seeing a doctor for serious concerns
3. Be empathetic, clear, and use simple language
4. Never diagnose conditions - only provide general information
5. Respect user privacy and handle medical data carefully

You have access to tools to:
- View and add medications
- View and schedule appointments
- Log health metrics
- Analyze health trends

When users ask about their medical data, use the appropriate tools to fetch and display the information.

MEDICAL DISCLAIMER: This assistant is for informational purposes only and should not replace professional medical advice, diagnosis, or treatment. Always consult with a qualified healthcare provider for medical concerns.
"""

# Initialize the medical agent
medical_agent = Agent(
    f'groq:{settings.GROQ_API_KEY}',
    model='llama-3.1-70b-versatile',
    deps_type=MedicalContext,
    system_prompt=SYSTEM_PROMPT,
    tools=[
        get_medications,
        add_medication,
        get_appointments,
        schedule_appointment,
        log_health_metric,
        get_health_trends
    ],
    retries=2
)

async def run_medical_agent(user_id: str, user_name: str, message: str) -> str:
    """
    Run the medical agent with user context
    
    Args:
        user_id: User ID
        user_name: User's name
        message: User's message
        
    Returns:
        Agent's response
    """
    try:
        context = MedicalContext(
            user_id=user_id,
            user_name=user_name
        )
        
        result = await medical_agent.run(
            message,
            deps=context
        )
        
        return result.data
        
    except Exception as e:
        logger.error(f"Error running medical agent: {e}")
        return "I'm having trouble processing your request right now. Please try again in a moment."
