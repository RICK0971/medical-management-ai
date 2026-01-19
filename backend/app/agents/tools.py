"""
Tools for the medical AI agent
"""

from typing import List, Dict, Any
from datetime import datetime, date, timedelta
from loguru import logger
from pydantic_ai import RunContext
from pydantic import BaseModel

from app.services.database import supabase

# Define MedicalContext here to avoid circular import
class MedicalContext(BaseModel):
    """Context passed to the agent"""
    user_id: str
    user_name: str

async def get_medications(ctx: RunContext[MedicalContext]) -> List[Dict[str, Any]]:
    """
    Get user's current medications
    
    Returns:
        List of active medications
    """
    try:
        response = supabase.table('medications').select('*').eq(
            'user_id', ctx.deps.user_id
        ).eq('active', True).execute()
        
        return response.data if response.data else []
    except Exception as e:
        logger.error(f"Error fetching medications: {e}")
        return []

async def add_medication(
    ctx: RunContext[MedicalContext],
    name: str,
    dosage: str,
    frequency: str,
    start_date: str,
    notes: str = ""
) -> Dict[str, Any]:
    """
    Add a new medication for the user
    
    Args:
        name: Medication name
        dosage: Dosage amount (e.g., "500mg")
        frequency: How often to take (e.g., "twice daily")
        start_date: Start date (YYYY-MM-DD)
        notes: Additional notes
        
    Returns:
        Created medication record
    """
    try:
        medication_data = {
            'user_id': ctx.deps.user_id,
            'name': name,
            'dosage': dosage,
            'frequency': frequency,
            'start_date': start_date,
            'notes': notes,
            'active': True
        }
        
        response = supabase.table('medications').insert(medication_data).execute()
        return response.data[0] if response.data else {}
    except Exception as e:
        logger.error(f"Error adding medication: {e}")
        return {"error": str(e)}

async def get_appointments(ctx: RunContext[MedicalContext]) -> List[Dict[str, Any]]:
    """
    Get user's upcoming appointments
    
    Returns:
        List of scheduled appointments
    """
    try:
        response = supabase.table('appointments').select('*').eq(
            'user_id', ctx.deps.user_id
        ).eq('status', 'scheduled').gte(
            'date_time', datetime.now().isoformat()
        ).order('date_time').execute()
        
        return response.data if response.data else []
    except Exception as e:
        logger.error(f"Error fetching appointments: {e}")
        return []

async def schedule_appointment(
    ctx: RunContext[MedicalContext],
    doctor_name: str,
    specialty: str,
    date_time: str,
    location: str,
    notes: str = ""
) -> Dict[str, Any]:
    """
    Schedule a new appointment
    
    Args:
        doctor_name: Doctor's name
        specialty: Medical specialty
        date_time: Appointment date and time (ISO format)
        location: Appointment location
        notes: Additional notes
        
    Returns:
        Created appointment record
    """
    try:
        appointment_data = {
            'user_id': ctx.deps.user_id,
            'doctor_name': doctor_name,
            'specialty': specialty,
            'date_time': date_time,
            'location': location,
            'notes': notes,
            'status': 'scheduled'
        }
        
        response = supabase.table('appointments').insert(appointment_data).execute()
        return response.data[0] if response.data else {}
    except Exception as e:
        logger.error(f"Error scheduling appointment: {e}")
        return {"error": str(e)}

async def log_health_metric(
    ctx: RunContext[MedicalContext],
    metric_type: str,
    value: str,
    unit: str,
    notes: str = ""
) -> Dict[str, Any]:
    """
    Log a health metric
    
    Args:
        metric_type: Type of metric (blood_pressure, blood_sugar, weight, etc.)
        value: Metric value
        unit: Unit of measurement
        notes: Additional notes
        
    Returns:
        Created health metric record
    """
    try:
        metric_data = {
            'user_id': ctx.deps.user_id,
            'metric_type': metric_type,
            'value': value,
            'unit': unit,
            'notes': notes,
            'recorded_at': datetime.now().isoformat()
        }
        
        response = supabase.table('health_metrics').insert(metric_data).execute()
        return response.data[0] if response.data else {}
    except Exception as e:
        logger.error(f"Error logging health metric: {e}")
        return {"error": str(e)}

async def get_health_trends(
    ctx: RunContext[MedicalContext],
    metric_type: str,
    days: int = 30
) -> List[Dict[str, Any]]:
    """
    Get health metric trends over time
    
    Args:
        metric_type: Type of metric to analyze
        days: Number of days to look back
        
    Returns:
        List of health metrics
    """
    try:
        from_date = (datetime.now() - timedelta(days=days)).isoformat()
        
        response = supabase.table('health_metrics').select('*').eq(
            'user_id', ctx.deps.user_id
        ).eq('metric_type', metric_type).gte(
            'recorded_at', from_date
        ).order('recorded_at').execute()
        
        return response.data if response.data else []
    except Exception as e:
        logger.error(f"Error fetching health trends: {e}")
        return []
