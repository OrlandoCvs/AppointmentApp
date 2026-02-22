from pydantic import BaseModel, Field, ConfigDict, EmailStr
from uuid import UUID, uuid4 as uuid
from typing import Optional

class Patient(BaseModel):
    uuid : UUID 
    first_name : str
    last_name : str
    model_config = ConfigDict(from_attributes=True)
    
class PatientCreate(BaseModel):
    first_name : str
    last_name : str
    email : EmailStr
    phone : Optional[str] = None
    model_config = ConfigDict(from_attributes=True)