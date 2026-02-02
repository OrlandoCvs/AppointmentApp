from pydantic import BaseModel, Field, ConfigDict
from uuid import UUID, uuid4 as uuid
from typing import Optional

class Doctor(BaseModel):
    uuid : UUID = Field(default_factory= uuid)
    doctor_name : str
    doctor_lastname : str
    specialty_uuid : UUID
    model_config = ConfigDict(from_attributes= True)

class DoctorList(BaseModel):
    doctor_name : str
    doctor_lastname : str
    specialty_name : Optional[str]
    model_config = ConfigDict(from_attributes=True)




