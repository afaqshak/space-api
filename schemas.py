from pydantic import BaseModel, Field

class OrbitRequest(BaseModel):
    # Usiamo Field per aggiungere documentazione e vincoli (es. altitudine > 0)
    altitude_km: float = Field(..., gt=0, description="Altitudine del satellite in km")

class OrbitResponse(BaseModel):
    altitude_km: float
    orbital_period_minutes: float
    velocity_km_s: float