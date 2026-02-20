from sqlalchemy import create_engine, text
from sqlalchemy.orm import declarative_base, sessionmaker # <--- Agrega sessionmaker
from sqlalchemy.schema import MetaData

# 1. Configuración básica
DATABASE_URL = "mysql+pymysql://root:@localhost:3306/appointmentdb"
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