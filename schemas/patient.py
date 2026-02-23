from pydantic import BaseModel, Field, ConfigDict, EmailStr
from datetime import date, datetime
from uuid import UUID, uuid4 as uui
from typing import Optional
from models.enums import GenderEnum

class Patient(BaseModel):
    uuid : UUID 
    first_name : str
    last_name : str
    email : EmailStr
    phone : str
    gender : GenderEnum
    birth_date : date 
    blood_type : str
    emergency_contact : Optional[str] = None

    created_at : datetime
    model_config = ConfigDict(from_attributes=True)

class PatientBasic(BaseModel):
    first_name: str
    last_name: str
    uuid : str
    model_config = ConfigDict(from_attributes=True)
    
class PatientCreate(BaseModel):
    first_name : str
    last_name : str
    email : EmailStr
    phone : Optional[str] = None
    model_config = ConfigDict(from_attributes=True)