from fastapi import APIRouter
from config.db import conn, engine
from models.appointment import appointments
from schemas.appointment import Appointment

from cryptography.fernet import Fernet


key = Fernet.generate_key()

f = Fernet(key)

appointment = APIRouter()

@appointment.get("/appointments")
def get_appointments():
    
    with engine.connect() as conn:
        
        result = conn.execute(appointments.select()).mappings().all()
    
    return result
    
@appointment.post("/appointments")
def create_appointment(appointment : Appointment):
    new_appointment = appointment.model_dump()
    new_appointment["description"] = f.encrypt(appointment.description.encode()).decode()
    
    with conn:
        conn.execute(appointments.insert().values(new_appointment))
        conn.commit()
    
    return {"message:" "cita creada con exito"}

@appointment.get("/doctors")
def get_doctors(doctor):
    return "Hello world"

