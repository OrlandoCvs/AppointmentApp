from pydantic import BaseModel, Field, ConfigDict
from uuid import UUID
from datetime import datetime
from typing import Optional, List
# Importamos el schema de Prescription que ya validamos
from schemas.prescription import Prescription

class AppointmentBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    description: str = Field(..., example="Dolor de garganta y fiebre")
    appointment_datetime: datetime

class AppointmentCreate(AppointmentBase):
    # En lugar de nombres, enviamos los IDs para vincular en la DB
    doctor_id: int
    patient_id: int

class AppointmentList(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    uuid: UUID
    appointment_datetime: datetime
    status: str
    # Aquí podrías incluir info básica del doctor/paciente para la lista
    doctor_name: Optional[str] = None 
    patient_name: Optional[str] = None

class Appointment(AppointmentBase):
    id: int
    uuid: UUID
    status: str
    created_at: datetime
    doctor_id: int
    patient_id: int
    
    # EL GRAN CAMBIO: Incluimos la receta de forma opcional
    # Si la cita no tiene receta aún, esto será None
    prescription: Optional[Prescription] = None