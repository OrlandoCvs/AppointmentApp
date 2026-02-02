from fastapi import FastAPI
from routes.appointment import appointment

app = FastAPI()

app.include_router(appointment)