from fastapi import FastAPI
from schemas import OrbitRequest, OrbitResponse
import math

app = FastAPI(title="Space Engineering API - PoliMi Edition")

# Costanti
G = 6.67430e-11  # m^3 kg^-1 s^-2
M_EARTH = 5.972e24 # kg
R_EARTH = 6371.0   # km

@app.get("/")
def root():
    return {"status": "online", "message": "Benvenuto Ingegnere. Vai su /docs"}

@app.post("/calculate", response_model=OrbitResponse)
def calculate_orbit(data: OrbitRequest):
    # Calcolo Semiasse Maggiore (in metri)
    a_meters = (R_EARTH + data.altitude_km) * 1000
    
    # Formula Periodo
    mu = G * M_EARTH
    period_seconds = 2 * math.pi * math.sqrt(math.pow(a_meters, 3) / mu)
    
    # Calcolo Velocità Orbitale v = sqrt(mu / a)
    velocity_ms = math.sqrt(mu / a_meters)
    
    return {
        "altitude_km": data.altitude_km,
        "orbital_period_minutes": round(period_seconds / 60, 2),
        "velocity_km_s": round(velocity_ms / 1000, 2)
    }
