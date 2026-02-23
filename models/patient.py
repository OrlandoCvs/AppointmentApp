from sqlalchemy import Column, text, ForeignKey
from sqlalchemy import Integer, String, DateTime, CHAR, Enum as SQLEnum, Date
from sqlalchemy.orm import relationship
from config.db import Base
from models.enums import GenderEnum
import uuid as uuid_pkg


class Patient(Base):
     __tablename__ = "patients"
     id = Column(Integer, primary_key = True, autoincrement=True)
     uuid = Column(CHAR(36), nullable= False, unique = True, default= lambda: str(uuid_pkg.uuid4()))
     first_name = Column(String(255), nullable= False)
     last_name = Column(String(255), nullable=False)
     email = Column(String(255), nullable=False, unique=True)
     phone = Column(String(20), nullable=False)
     gender = Column(SQLEnum(GenderEnum), nullable=False)
     birth_date = Column(Date, nullable=False)
     blood_type = Column(String(5), nullable=True)

     #Relationships
     appointments = relationship("Appointment", back_populates="patient")
     