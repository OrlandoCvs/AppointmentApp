from sqlalchemy import Column, text, ForeignKey
from sqlalchemy import Integer, String, DateTime, CHAR
from sqlalchemy.orm import relationship
from config.db import Base
import uuid

class Specialty(Base):
    __tablename__ = "specialties"
    id = Column(Integer, primary_key= True, autoincrement=True)
    #UUID 
    uuid = Column(CHAR(36), unique=True, index=True, nullable=False, default = lambda: str(uuid.uuid4()))
    name = Column(String(255), unique = True, nullable=False)
    description = Column(String(1000), nullable= True)
    doctors = relationship("Doctor", back_populates="specialty")