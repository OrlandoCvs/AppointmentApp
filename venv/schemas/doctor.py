from pydantic import BaseModel, Field, ConfigDict, EmailStr
from uuid import UUID, uuid4 as uuid
from typing import Optional

class SpecialtyBasic(BaseModel):
    name: str
    uuid: UUID 
    model_config = ConfigDict(from_attributes=True)

class Doctor(BaseModel):
    uuid : UUID = Field(default_factory= uuid)
    doctor_name : str
    doctor_lastname : str
    specialty_uuid : UUID
    model_config = ConfigDict(from_attributes= True)
    email : EmailStr 

class DoctorList(BaseModel):
    uuid : UUID 
    doctor_name : str
    doctor_lastname : str
    specialty : SpecialtyBasic
    model_config = ConfigDict(from_attributes=True)





