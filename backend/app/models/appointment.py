"""
Appointment models
"""

from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from enum import Enum

class AppointmentStatus(str, Enum):
    SCHEDULED = "scheduled"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

class AppointmentBase(BaseModel):
    doctor_name: str
    specialty: str
    date_time: datetime
    location: str
    notes: Optional[str] = None

class AppointmentCreate(AppointmentBase):
    pass

class AppointmentUpdate(BaseModel):
    doctor_name: Optional[str] = None
    specialty: Optional[str] = None
    date_time: Optional[datetime] = None
    location: Optional[str] = None
    notes: Optional[str] = None
    status: Optional[AppointmentStatus] = None

class Appointment(AppointmentBase):
    id: str
    user_id: str
    status: AppointmentStatus = AppointmentStatus.SCHEDULED
    created_at: datetime
    
    class Config:
        from_attributes = True
