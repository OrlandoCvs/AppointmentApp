from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime
from typing import Optional
from uuid import UUID


class MedicationBase(BaseModel):
    name: str = Field(..., example="Amoxicilina", description="Nombre del medicamento")
    dosage: str = Field(..., example="500mg", description="Dosis (ej. 1 tableta, 5ml)")
    
    frequency_hours: int = Field(..., gt=0, le=24, example=8, description="Cada cuántas horas se toma")
    duration_days: int = Field(..., gt=0, example=7, description="Por cuántos días")
    start_datetime: datetime = Field(..., description="Fecha y hora de la primera dosis")
    notifications_enabled: bool = Field(default=True, description="¿Desea recibir alertas?")
    model_config = ConfigDict(from_attributes=True)

class MedicationCreate(MedicationBase):
    prescription_id: int
    

class Medication(MedicationBase):
    id: int
    uuid : UUID
    
