from sqlalchemy import Column, text, ForeignKey
from sqlalchemy import Integer, String, DateTime, CHAR
from sqlalchemy.orm import relationship
from config.db import Base
import uuid


class Doctor(Base):
    __tablename__ = "doctors"
    id = Column(Integer, primary_key= True, autoincrement= True)
    uuid = Column(CHAR(36), unique= True, nullable=False, index= True, default=lambda:str(uuid.uuid4()))
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    specialty_id = Column(Integer, ForeignKey("specialties.id"), nullable=False)
    specialty = relationship("Specialty", back_populates= "doctors" )
    appointments = relationship("Appointment", back_populates= "doctor")
    email = Column(String(255), index=True, nullable=False, unique= True)

