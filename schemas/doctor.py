from pydantic import BaseModel, Field, ConfigDict, EmailStr
from uuid import UUID, uuid4 as uuid
from typing import Optional
from schemas.specialty import SpecialtyBasic


class Doctor(BaseModel):
    uuid : UUID = Field(default_factory= uuid)
    doctor_name : str
    doctor_lastname : str
    specialty_uuid : UUID
    model_config = ConfigDict(from_attributes= True)
    email : EmailStr 

class DoctorBasic(BaseModel):
    uuid : UUID 
    first_name : str
    last_name : str
    specialty : SpecialtyBasic
    model_config = ConfigDict(from_attributes=True)

class DoctorCreate(BaseModel):
    first_name : str
    last_name : str
    email : EmailStr
    specialty_uuid: UUID





