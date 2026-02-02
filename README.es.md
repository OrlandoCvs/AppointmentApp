# Technical Documentation: Appointment Management System

**Document Version:** 1.0

**Date:** February 1, 2026 

**Project Status:** Development (Modeling & Migration Phase)

## 1. Database Configuration

The system utilizes **SQLAlchemy** as the ORM (Object-Relational Mapping) to interact with a MySQL database. The connection is managed via the `pymysql` driver.

### 1.1 Connection Engine

The configuration file establishes the connection and performs an immediate validation to ensure service availability.

**Source Code (`config/db.py`):**

```python
# Engine definition with MySQL connection string
engine = create_engine("mysql+pymysql://root:@localhost:3306/appointmentdb")

# Startup connectivity validation
try:
    with engine.connect() as conn:
        conn.execute(text("SELECT 1")) # Lightweight test query
        print("Successful connection to the database!")  
except Exception as e:
    print(f"Connection error: {e}")

```

---

## 2. Identification Strategy (Hybrid ID Pattern)

To balance database performance with API security, a dual identification strategy is implemented across all primary entities.

1. 
**Primary Key (Internal):** `Integer` auto-increment. Used for relationships (`ForeignKey`) and internal MySQL indexing due to its efficiency.


2. 
**Public ID (External):** `UUID` (Universally Unique Identifier). Exposed in Pydantic Schemas to prevent resource enumeration by malicious users.



**Standard Model Implementation:**

```python
# Example from models/appointment.py
id = Column(Integer, primary_key=True, autoincrement=True)
uuid = Column(CHAR(36), unique=True, index=True, nullable=False, default=lambda: str(uuid.uuid4()))

```

---

## 3. Data Model Definitions (ORM)

Models inherit from `declarative_base` and define the physical structure of the tables.

### 3.1 Entity: Doctor (`models/doctor.py`)

Represents the medical professional. Includes uniqueness validation for email and bidirectional relationships.

* **Relationships:**
* 
`specialty`: *Many-to-One* relationship with the specialties table.


* 
`appointments`: *One-to-Many* relationship with scheduled appointments.





```python
class Doctor(Base):
    __tablename__ = "doctors"
    # ... id and uuid columns ...
    doctor_name = Column(String(255), nullable=False)
    email = Column(String(255), index=True, nullable=False, unique=True)
    
    # Database level Foreign Key
    specialty_id = Column(Integer, ForeignKey("specialties.id"), nullable=False)
    
    # ORM level Relationships
    specialty = relationship("Specialty", back_populates="doctors")
    appointments = relationship("Appointment", back_populates="doctor")

```

### 3.2 Entity: Appointment (`models/appointment.py`)

Primary transactional table. Currently stores patient data as plain text (legacy), awaiting normalization.

* 
**Indexes:** `index=True` is defined on `doctor_id` to optimize schedule queries by physician.



```python
class Appointment(Base):
    __tablename__ = "appointments"
    # ...
    description = Column(String(1000), nullable=False)
    appointment_datetime = Column(DateTime, nullable=False)
    status = Column(String(50), server_default=text("'pending'"))
    
    # Relationship with Doctor
    doctor_id = Column(Integer, ForeignKey("doctors.id"), nullable=False, index=True)
    doctor = relationship("Doctor", back_populates="appointments")

```

### 3.3 Entity: Patient (`models/patient.py`)

New entity incorporated via migration. Currently operates as a standalone table.

```python
class Patient(Base):
     __tablename__ = "patients"
     id = Column(Integer, primary_key=True, autoincrement=True)
     uuid = Column(CHAR(36), nullable=False, unique=True, default=lambda: str(uuid.uuid4()))
     patient_name = Column(String(255), nullable=False)
     patient_lastname = Column(String(255), nullable=False)

```

---

## 4. Validation Layer (Pydantic Schemas)

Schemas decouple the database logic from the public API interface, handling type validation and serialization.

### 4.1 General Configuration

All schemas utilize `ConfigDict(from_attributes=True)` to allow Pydantic to read SQLAlchemy ORM objects directly.

### 4.2 Doctor Validation (`schemas/doctor.py`)

`EmailStr` is implemented to ensure the email format is valid before attempting database insertion.

```python
class Doctor(BaseModel):
    uuid: UUID = Field(default_factory=uuid) # Auto-generation if not provided
    doctor_name: str
    email: EmailStr  # Automatic format validation
    specialty_uuid: UUID
    model_config = ConfigDict(from_attributes=True)

```

### 4.3 Appointment Validation (`schemas/appointment.py`)

Creation and Read schemas are separated to control data exposure.

* 
**AppointmentCreate:** Requests only essential data from the user.


* 
**AppointmentList:** Exposes the public `uuid` but hides the internal `id` (Integer).



```python
class AppointmentList(BaseModel):
    uuid: UUID
    patient_name: str
    appointment_datetime: datetime
    status: str
    model_config = ConfigDict(from_attributes=True)

```

---

## 5. Database Version Control (Alembic)

The project uses Alembic to manage schema evolution without data loss.

**Current Status:**

* 
**Revision ID:** `6911a0f4dee9` 


* 
**Recent Change:** Creation of the `patients` table.



**Generated Migration Script:**
The `upgrade()` method executes the DDL commands required to create the table with its constraints (`PrimaryKey` and `UniqueConstraint`).

```python
def upgrade() -> None:
    op.create_table('patients',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('uuid', sa.CHAR(length=36), nullable=False),
        sa.Column('patient_name', sa.String(length=255), nullable=False),
        # ... additional columns ...
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('uuid')
    )




