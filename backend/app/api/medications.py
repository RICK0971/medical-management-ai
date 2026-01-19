"""
Medications API routes
"""

from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from loguru import logger
import uuid

from app.models.medication import Medication, MedicationCreate, MedicationUpdate
from app.services.auth_service import get_current_user
from app.services.database import supabase

router = APIRouter()

@router.get("/", response_model=List[Medication])
async def get_medications(
    active_only: bool = True,
    current_user: dict = Depends(get_current_user)
):
    """Get user's medications"""
    try:
        query = supabase.table('medications').select('*').eq('user_id', current_user['id'])
        
        if active_only:
            query = query.eq('active', True)
        
        response = query.order('created_at', desc=True).execute()
        
        return response.data if response.data else []
        
    except Exception as e:
        logger.error(f"Error fetching medications: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to fetch medications"
        )

@router.post("/", response_model=Medication, status_code=status.HTTP_201_CREATED)
async def create_medication(
    medication: MedicationCreate,
    current_user: dict = Depends(get_current_user)
):
    """Create a new medication"""
    try:
        medication_data = {
            'id': str(uuid.uuid4()),
            'user_id': current_user['id'],
            **medication.dict(),
            'active': True
        }
        
        response = supabase.table('medications').insert(medication_data).execute()
        
        if not response.data:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to create medication"
            )
        
        return response.data[0]
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error creating medication: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create medication"
        )

@router.get("/{medication_id}", response_model=Medication)
async def get_medication(
    medication_id: str,
    current_user: dict = Depends(get_current_user)
):
    """Get a specific medication"""
    try:
        response = supabase.table('medications').select('*').eq(
            'id', medication_id
        ).eq('user_id', current_user['id']).execute()
        
        if not response.data:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Medication not found"
            )
        
        return response.data[0]
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error fetching medication: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to fetch medication"
        )

@router.patch("/{medication_id}", response_model=Medication)
async def update_medication(
    medication_id: str,
    medication_update: MedicationUpdate,
    current_user: dict = Depends(get_current_user)
):
    """Update a medication"""
    try:
        # Verify ownership
        existing = supabase.table('medications').select('*').eq(
            'id', medication_id
        ).eq('user_id', current_user['id']).execute()
        
        if not existing.data:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Medication not found"
            )
        
        # Update
        update_data = medication_update.dict(exclude_unset=True)
        
        response = supabase.table('medications').update(update_data).eq(
            'id', medication_id
        ).execute()
        
        return response.data[0]
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error updating medication: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to update medication"
        )

@router.delete("/{medication_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_medication(
    medication_id: str,
    current_user: dict = Depends(get_current_user)
):
    """Delete a medication (soft delete by setting active=False)"""
    try:
        # Verify ownership
        existing = supabase.table('medications').select('*').eq(
            'id', medication_id
        ).eq('user_id', current_user['id']).execute()
        
        if not existing.data:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Medication not found"
            )
        
        # Soft delete
        supabase.table('medications').update({'active': False}).eq(
            'id', medication_id
        ).execute()
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error deleting medication: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to delete medication"
        )
