from pydantic import BaseModel, Field, ConfigDict, EmailStr
from uuid import UUID, uuid4 as uuid
from typing import Optional

class Patient(BaseModel):
    uuid = UUID = Field(default_factory= uuid)
    patient_name = str
    patient_lastname = str
    