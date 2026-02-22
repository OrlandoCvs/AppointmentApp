from pydantic import BaseModel, Field, ConfigDict
from uuid import UUID, uuid4 as uuid
from typing import Optional

class SpecialtyBasic(BaseModel):
    uuid : UUID = Field(default_factory=uuid)
    name : str


