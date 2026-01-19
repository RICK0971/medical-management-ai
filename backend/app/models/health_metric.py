"""
Health Metric models
"""

from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from enum import Enum

class MetricType(str, Enum):
    BLOOD_PRESSURE = "blood_pressure"
    BLOOD_SUGAR = "blood_sugar"
    WEIGHT = "weight"
    TEMPERATURE = "temperature"
    HEART_RATE = "heart_rate"
    OXYGEN_SATURATION = "oxygen_saturation"

class HealthMetricBase(BaseModel):
    metric_type: MetricType
    value: str  # Can be "120/80" for BP or "98.6" for temp
    unit: str
    notes: Optional[str] = None

class HealthMetricCreate(HealthMetricBase):
    recorded_at: Optional[datetime] = None

class HealthMetric(HealthMetricBase):
    id: str
    user_id: str
    recorded_at: datetime
    created_at: datetime
    
    class Config:
        from_attributes = True
