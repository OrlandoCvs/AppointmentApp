from sqlalchemy import Column, text, ForeignKey
from sqlalchemy import Integer, String, DateTime, CHAR
from sqlalchemy.orm import relationship
from config.db import Base
import uuid

class Patient(Base):
     __tablename__ = "patients"
     id = Column(Integer, primary_key = True, autoincrement=True)
     uuid = Column(CHAR(36), nullable= False, unique = True, default= lambda: str(uuid.uuid4()))
     patient_name = Column(String(255), nullable= False)
     patient_lastname = Column(String(255), nullable=False)


     