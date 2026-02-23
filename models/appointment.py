from sqlalchemy import Column, text, ForeignKey
from sqlalchemy import Integer, String, DateTime, CHAR
from sqlalchemy.orm import relationship
from config.db import Base
import uuid as uuid_pkg

class Appointment(Base):
    __tablename__ = "appointments"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    uuid = Column(CHAR(36), unique=True, index=True, nullable=False, default=lambda: str(uuid_pkg.uuid4()))
    
    description = Column(String(1000), nullable=False)
    appointment_datetime = Column(DateTime, nullable=False)
    
    status = Column(String(50), server_default=text("'pending'"))
    created_at = Column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    updated_at = Column(DateTime, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    
    doctor_id = Column(Integer, ForeignKey("doctors.id"), nullable=False, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"), nullable=False, index=True)

    # RELATIONS - Usando Strings para evitar el error de localización
    doctor = relationship("Doctor", back_populates="appointments")
    patient = relationship("Patient", back_populates="appointments")
    
    # Nota: Cambié "appointments" por "appointment" para que coincida con tu modelo de Prescription
    prescription = relationship("Prescription", back_populates="appointment", uselist=False)