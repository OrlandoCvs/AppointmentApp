from sqlalchemy import create_engine, text
from sqlalchemy.orm import declarative_base, sessionmaker # <--- Agrega sessionmaker
from sqlalchemy.schema import MetaData
import os 
from dotenv import load_dotenv
# 1. Configuración básica

load_dotenv()

DB_USER = "root"
DB_PASS = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL)

# 2. Crear la fábrica de sesiones (ESTO TE FALTA)
# Esto permitirá crear una sesión única por cada petición a la API
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# 3. Función de Dependencia (ESTO ES VITAL PARA FASTAPI)
# Esta función abre una sesión y la cierra automáticamente al terminar la petición
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Tu prueba de conexión actual (está bien dejarla para validar)
try:
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))
        print("¡Conexión exitosa a la base de datos!")
except Exception as e:
    print(f"Error al conectar: {e}")