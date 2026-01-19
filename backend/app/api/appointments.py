"""
Appointments API routes
"""

from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from loguru import logger
import uuid

from app.models.appointment import Appointment, AppointmentCreate, AppointmentUpdate
from app.services.auth_service import get_current_user
from app.services.database import supabase

router = APIRouter()

@router.get("/", response_model=List[Appointment])
async def get_appointments(
    current_user: dict = Depends(get_current_user)
):
    """Get user's appointments"""
    try:
        response = supabase.table('appointments').select('*').eq(
            'user_id', current_user['id']
        ).order('date_time', desc=False).execute()
        
        return response.data if response.data else []
        
    except Exception as e:
        logger.error(f"Error fetching appointments: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to fetch appointments"
        )

@router.post("/", response_model=Appointment, status_code=status.HTTP_201_CREATED)
async def create_appointment(
    appointment: AppointmentCreate,
    current_user: dict = Depends(get_current_user)
):
    """Create a new appointment"""
    try:
        appointment_data = {
            'id': str(uuid.uuid4()),
            'user_id': current_user['id'],
            **appointment.dict(),
            'status': 'scheduled'
        }
        
        response = supabase.table('appointments').insert(appointment_data).execute()
        
        if not response.data:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to create appointment"
            )
        
        return response.data[0]
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error creating appointment: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create appointment"
        )

@router.patch("/{appointment_id}", response_model=Appointment)
async def update_appointment(
    appointment_id: str,
    appointment_update: AppointmentUpdate,
    current_user: dict = Depends(get_current_user)
):
    """Update an appointment"""
    try:
        # Verify ownership
        existing = supabase.table('appointments').select('*').eq(
            'id', appointment_id
        ).eq('user_id', current_user['id']).execute()
        
        if not existing.data:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Appointment not found"
            )
        
        # Update
        update_data = appointment_update.dict(exclude_unset=True)
        
        response = supabase.table('appointments').update(update_data).eq(
            'id', appointment_id
        ).execute()
        
        return response.data[0]
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error updating appointment: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to update appointment"
        )

@router.delete("/{appointment_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_appointment(
    appointment_id: str,
    current_user: dict = Depends(get_current_user)
):
    """Delete an appointment"""
    try:
        # Verify ownership
        existing = supabase.table('appointments').select('*').eq(
            'id', appointment_id
        ).eq('user_id', current_user['id']).execute()
        
        if not existing.data:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Appointment not found"
            )
        
        # Delete
        supabase.table('appointments').delete().eq('id', appointment_id).execute()
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error deleting appointment: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to delete appointment"
        )
