from sqlalchemy import Column, text, ForeignKey
from sqlalchemy import Integer, String, DateTime, CHAR
from sqlalchemy.orm import relationship
from config.db import Base
import uuid as uuid_pkg


class Doctor(Base):
    __tablename__ = "doctors"
    id = Column(Integer, primary_key= True, autoincrement= True)
    uuid = Column(CHAR(36), unique= True, nullable=False, index= True, default=lambda:str(uuid_pkg.uuid4()))
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)

    email = Column(String(255), index=True, nullable=False, unique= True)

    #Field for the Medical License (It may change depending on the country that is using this sistem).

    license_number = Column(String(50), unique= True , nullable=True)

    #Links for doctor's id and medical license to verify doctor's identity
    id_card_url = Column(String(500), nullable= True) 
    license_url = Column(String(500), nullable= True)

    #Small descriptionn or biography provided by the doctor
    bio = Column(String(1000), nullable=True)
    


    #Status managment
    is_active = Column(Integer, server_default=text("1"))
    is_verified = Column(Integer, server_default=text("0"))


    #Relationships
    specialty_id = Column(Integer, ForeignKey("specialties.id"), nullable=False)
    specialty = relationship("Specialty", back_populates= "doctors" )
    appointments = relationship("Appointment", back_populates= "doctor")






