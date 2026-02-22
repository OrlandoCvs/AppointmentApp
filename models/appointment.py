#models/appointment.py: Defines the physical table structure in MySql.

#uses SQLAlchemy Table constructs to map columns, data types. and constraints.

#uses two ID's: UUID for safe handling and conventional ID for DB porpuses and efficency.

from sqlalchemy import Column, text, ForeignKey
from sqlalchemy import Integer, String, DateTime, CHAR
from sqlalchemy.orm import relationship
from config.db import Base
from models.patient import Patient
import uuid



class Appointment(Base):
    __tablename__ = "appointments"
    id = Column(Integer, primary_key= True, autoincrement=True)
    uuid = Column(CHAR(36), unique= True, index=True, nullable=False, default= lambda: str(uuid.uuid4()))
    description = Column(String(1000), nullable= False)
    appointment_datetime = Column(DateTime, nullable=False)
    status = Column(String(50), server_default= text("'pending'"))
    created_at = Column(DateTime, server_default= text('CURRENT_TIMESTAMP'))
    doctor_id = Column(Integer, ForeignKey("doctors.id"), nullable=False, index= True)
    patient_id = Column(Integer, ForeignKey("patients.id"), nullable=False, index=True)

    #RELATIONS
    doctor = relationship("Doctor", back_populates= "appointments")
    patient = relationship("Patient", back_populates="appointments")


    

    


 


