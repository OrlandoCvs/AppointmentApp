#models/appointment.py: Defines the physical table structure in MySql.

#uses SQLAlchemy Table constructs to map columns, data types. and constraints.

#uses two ID's: UUID for safe handling and conventional ID for DB porpuses and efficency.

from sqlalchemy import Table,Column, text, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, DateTime, CHAR
from sqlalchemy.orm import declarative_base, relationship

from config.db import meta, engine
from datetime import datetime
import uuid

Base = declarative_base()

class Appointments(Base):
    __tablename__ = "appointments"
    id = Column(Integer, primary_key= True, autoincrement=True)
    uuid = Column(CHAR(36), unique= True, nullable=False, default= lambda: str(uuid.uuid4()))
    patient_name = Column(String(255), nullable= False)
    patient_lastname = Column(String(255), nullable= False)
    description = Column(String(1000), nullable= False)
    appointment_datetime = Column(DateTime, nullable=False)
    status = Column(String(50), server_default= text("'pending'"))
    created_at = Column(DateTime, server_default= text('CURRENT_TIMESTAMP'))

    doctor_id = Column(Integer, ForeignKey("doctors.id"), nullable=False)

    doctor = relationship("Doctor", back_populates= "appointments")
    

class Doctor(Base):
    __tablename__ = "doctors"
    id = Column(Integer, primary_key= True, autoincrement= True)
    uuid = Column(CHAR(36), unique= True, nullable=False, index= True, default=lambda:str(uuid.uuid4()))
    doctor_name = Column(String(255), nullable=False)
    doctor_lastname = Column(String(255), nullable=False)
    specialty_id = Column(Integer, ForeignKey("specialties.id"), nullable=False)
    specialty = relationship("Specialty", back_populates= "doctors" )
    appointments = relationship("Appointments", back_populates= "doctor")
    
class Specialty(Base):
    __tablename__ = "specialties"

    id = Column(Integer, primary_key= True, autoincrement=True)

    #UUID 
    uuid = Column(CHAR(36), unique=True, nullable=False, index= True, default = lambda: str(uuid.uuid4()))

    name = Column(String(255), unique = True, nullable=False)
    description = Column(String(1000), nullable= True)
    doctors = relationship("Doctor", back_populates="specialty")

meta.create_all(engine)
 


