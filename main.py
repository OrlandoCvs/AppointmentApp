# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel, Field
# from datetime import datetime, time
# from uuid import uuid4 as uuid, UUID

# app = FastAPI()

# @app.get("/")
# def root():
#     return {"mensaje":"HOLA"}

# appointments = []


# # POST MODEL

# class Appointment(BaseModel):
#     id: UUID = Field(default_factory = uuid)
#     patient_name :str
#     patient_lastname : str
#     description : str
#     appointment_datetime : datetime
#     doctor_id : UUID
#     created_at : datetime = Field(default_factory=datetime.now)
    

# @app.get('/posts')
# def get_posts():
#     return appointments

# @app.post('/posts')
# def save_post(appointment: Appointment):
#     appointment.id = str(uuid())
#     appointments.append(appointment.model_dump())
#     return appointments[-1]

# @app.get('/posts/{post_id}')
# def get_post(post_id : str):
#     for appointment in appointments:
#         if appointment["id"] == post_id:
#             return appointment
#     raise HTTPException(status_code=404, detail= "Post Not Found")

# @app.delete("/posts/{post_id}")
# def delete_post(post_id:str):
#     for i, appointment in enumerate(appointments):
#         if appointment["id"] == post_id:
#             appointments.pop(i)
#             return {"message" : "Post has been deleted succesfully"}

#     raise HTTPException(status_code=404, detail= "Post Not Found")

# @app.put('/posts/{post_id}')
# def update_post(post_id : str, updatedPost : Appointment):
#     for i, appointment in enumerate(appointments):
#         if appointment["id"] ==  post_id:
#             appointments[i]["patient_name"] = updatedPost.patient_name
#             appointments[i]["patient_lastname"] = updatedPost.patient_lastname
#             return {"message" : "Post has been updated succesfully "}
#     raise HTTPException(status_code=404, detail= "Post Not Found")
 