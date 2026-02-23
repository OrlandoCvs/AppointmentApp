from sqlalchemy import Column, text, ForeignKey
from sqlalchemy import Integer, String, DateTime, CHAR, Text
from sqlalchemy.orm import relationship
from config.db import Base
import uuid as uuid_pkg



class Medication(Base):
    __tablename__ = "medications"
    uuid = Column(CHAR(36), unique= True, index=True, nullable=False, default=lambda : str(uuid_pkg.uuid4()))
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False) 
    dosage = Column(String(100), nullable=False) 
    frequency_hours = Column(Integer, nullable=False) 
    duration_days = Column(Integer, nullable=False) 
    start_datetime = Column(DateTime, nullable=False)
    notifications_enabled = Column(Integer, server_default=text("1"))
    prescription_id = Column(Integer, ForeignKey("prescriptions.id"), nullable=False)
    prescription = relationship("Prescription", back_populates="medications")