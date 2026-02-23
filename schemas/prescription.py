from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime
from typing import List, Optional
from uuid import UUID
from schemas.medication import Medication, MedicationBase

class PrescriptionBase(BaseModel):
    diagnosis: str
    general_notes : Optional[str] = None
    model_config = ConfigDict(from_attributes=True)

class PrescriptionCreate(PrescriptionBase):
    appointment_id: int
    medications : List[MedicationBase] = []
   

class Prescription(PrescriptionBase):
    id : int
    uuid : UUID
    created_at : datetime
    medications : List[Medication] = []
