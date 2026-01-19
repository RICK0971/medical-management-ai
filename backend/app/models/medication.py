"""
Medication models
"""

from pydantic import BaseModel
from typing import Optional
from datetime import datetime, date

class MedicationBase(BaseModel):
    name: str
    dosage: str
    frequency: str
    start_date: date
    end_date: Optional[date] = None
    notes: Optional[str] = None

class MedicationCreate(MedicationBase):
    pass

class MedicationUpdate(BaseModel):
    name: Optional[str] = None
    dosage: Optional[str] = None
    frequency: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    notes: Optional[str] = None
    active: Optional[bool] = None

class Medication(MedicationBase):
    id: str
    user_id: str
    active: bool = True
    created_at: datetime
    
    class Config:
        from_attributes = True
