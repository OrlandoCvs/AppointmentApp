from sqlalchemy import Column, text, ForeignKey
from sqlalchemy import Integer, String, DateTime, CHAR, Text
from sqlalchemy.orm import relationship
from config.db import Base
import uuid as uuid_pkg

class Prescription(Base):
    __tablename__ = "prescriptions"
    id = Column(Integer, primary_key=True, autoincrement=True)
    uuid = Column(CHAR(36), unique=True, index=True, nullable=False, default=lambda: str(uuid_pkg.uuid4()))
    general_notes = Column(Text, nullable=True)
    diagnosis = Column(String(500), nullable=False)
    appointment_id = Column(Integer, ForeignKey("appointments.id"), nullable=False, unique=True)
    created_at = Column(DateTime, server_default=text('CURRENT_TIMESTAMP'))

    appointment = relationship("Appointment", back_populates="prescription")
    medications = relationship("Medication", back_populates="prescription", cascade="all, delete-orphan")