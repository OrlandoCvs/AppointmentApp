from pydantic import BaseModel, Field, ConfigDict
from uuid import UUID, uuid4 as uuid
from typing import Optional

class Specialty(BaseModel):
    id : int
    specialty_uuid : UUID = Field(default_factory=uuid())
    specialty_name : str


