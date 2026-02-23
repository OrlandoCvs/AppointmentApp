from sqlalchemy import Column, text, ForeignKey
from sqlalchemy import Integer, String, DateTime, CHAR
from sqlalchemy.orm import relationship
from config.db import Base
import uuid as uuid_pkg

class Specialty(Base):
    __tablename__ = "specialties"
    id = Column(Integer, primary_key= True, autoincrement=True)
    #UUID 
    uuid = Column(CHAR(36), unique=True, index=True, nullable=False, default = lambda: str(uuid_pkg.uuid4()))
    name = Column(String(255), unique = True, nullable=False)
    description = Column(String(1000), nullable= True)
    icon_url = Column(String(500), nullable=True)

    #Status managment
    is_active = Column(Integer, server_default = text("1"))

    #Relationships
    doctors = relationship("Doctor", back_populates="specialty")