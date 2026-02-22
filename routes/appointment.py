from fastapi import APIRouter, Depends, HTTPException
from config.db import engine, get_db
from sqlalchemy.orm import Session
from typing import List
from cryptography.fernet import Fernet
from schemas.doctor import DoctorBasic
# 1. IMPORTACIONES CLARAS
from models.appointment import Appointment as AppointmentDB
from models.doctor import Doctor as DoctorDB
from models.specialty import Specialty as SpecialtyDB
from schemas.appointment import Appointment as AppointmentSchema, AppointmentList

# Clave de encriptación (Ojo: en producción esto debe ser una variable de entorno fija)
key = Fernet.generate_key()
f = Fernet(key)

appointment = APIRouter()

# --- RUTA PARA OBTENER CITAS ---
@appointment.get("/appointments", response_model=List[AppointmentList])
def get_appointments(db: Session = Depends(get_db)): # Usa get_db siempre
    # Buscamos usando el MODELO de SQLAlchemy
    appointments = db.query(AppointmentDB).all()
    
    for a in appointments:
        try:
            # Desencriptamos la descripción antes de enviarla
            a.description = f.decrypt(a.description.encode()).decode()
        except Exception:
            pass # Por si hay datos no encriptados previos
            
    return appointments

# --- RUTA PARA CREAR CITA ---
@appointment.post("/appointments")
def create_appointment(data: AppointmentSchema, db: Session = Depends(get_db)):
    # 1. Convertimos el Schema de Pydantic a un diccionario
    appointment_data = data.model_dump()
    
    # 2. Encriptamos el campo sensible
    encrypted_desc = f.encrypt(data.description.encode()).decode()
    appointment_data["description"] = encrypted_desc
    
    # 3. Creamos el objeto del MODELO con los datos
    new_appointment = AppointmentDB(**appointment_data)
    
    # 4. Guardamos con SQLAlchemy
    db.add(new_appointment)
    db.commit()
    db.refresh(new_appointment)
    
    return {"message": "cita creada con éxito"}

# --- RUTA PARA DOCTORES ---
@appointment.get("/doctors", response_model= List[DoctorBasic])
def get_doctors(db: Session = Depends(get_db)):
    return db.query(DoctorDB).all()

@appointment.get("/specialties")
def get_specialties(db: Session = Depends(get_db)):
    return db.query(SpecialtyDB).all()