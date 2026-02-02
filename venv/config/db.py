from sqlalchemy import create_engine, MetaData, text
from sqlalchemy.orm import declarative_base

Base = declarative_base()
engine = create_engine("mysql+pymysql://root:@localhost:3306/appointmentdb")

try:
    # 2. Intentamos conectar y ejecutar una consulta mínima de validación
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))
        print("¡Conexión exitosa a la base de datos!")  
        
except Exception as e:
    # 3. Si algo sale mal, capturamos el error
    print(f"Error al conectar: {e}")

meta = MetaData()


