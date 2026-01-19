"""
Health Metrics API routes
"""

from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from loguru import logger
import uuid
from datetime import datetime

from app.models.health_metric import HealthMetric, HealthMetricCreate
from app.services.auth_service import get_current_user
from app.services.database import supabase

router = APIRouter()

@router.get("/", response_model=List[HealthMetric])
async def get_health_metrics(
    metric_type: str = None,
    current_user: dict = Depends(get_current_user)
):
    """Get user's health metrics"""
    try:
        query = supabase.table('health_metrics').select('*').eq('user_id', current_user['id'])
        
        if metric_type:
            query = query.eq('metric_type', metric_type)
        
        response = query.order('recorded_at', desc=True).execute()
        
        return response.data if response.data else []
        
    except Exception as e:
        logger.error(f"Error fetching health metrics: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to fetch health metrics"
        )

@router.post("/", response_model=HealthMetric, status_code=status.HTTP_201_CREATED)
async def create_health_metric(
    metric: HealthMetricCreate,
    current_user: dict = Depends(get_current_user)
):
    """Log a new health metric"""
    try:
        metric_data = {
            'id': str(uuid.uuid4()),
            'user_id': current_user['id'],
            **metric.dict(),
            'recorded_at': metric.recorded_at or datetime.now()
        }
        
        response = supabase.table('health_metrics').insert(metric_data).execute()
        
        if not response.data:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to log health metric"
            )
        
        return response.data[0]
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error creating health metric: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to log health metric"
        )

@router.delete("/{metric_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_health_metric(
    metric_id: str,
    current_user: dict = Depends(get_current_user)
):
    """Delete a health metric"""
    try:
        # Verify ownership
        existing = supabase.table('health_metrics').select('*').eq(
            'id', metric_id
        ).eq('user_id', current_user['id']).execute()
        
        if not existing.data:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Health metric not found"
            )
        
        # Delete
        supabase.table('health_metrics').delete().eq('id', metric_id).execute()
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error deleting health metric: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to delete health metric"
        )
