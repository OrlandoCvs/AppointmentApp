#schemas/appointments.py: focuses on Data Validation (how data enters the API)

#pydantic schemas handle Request/Response data validation and serialization.
#ensures incoming JSON matches expected types before reaching the database.
#separates internal logic from public facing data.

from pydantic import BaseModel, Field, ConfigDict
from uuid import UUID, uuid4 as uuid
from datetime import datetime

#because we don't need to create ID's
from typing import Optional


class Appointment(BaseModel):
    uuid: UUID = Field(default_factory = uuid)
    patient_name :str
    patient_lastname : str
    description : str
    appointment_datetime : datetime
    doctor_id : UUID
    status: str = "pending"
    created_at : Optional[datetime] = None
    #DB objects compatibility with SQLAlchemy
    model_config = ConfigDict(from_attributes=True)

class AppointmentList(BaseModel):
    uuid: UUID
    patient_name : str
    patient_lastname : str
    appointment_datetime : datetime
    status: str
    model_config = ConfigDict(from_attributes=True)

class AppointmentCreate(BaseModel):
    patient_name: str
    patient_lastname: str
    description: str
    model_config = ConfigDict(from_attributes=True)


    