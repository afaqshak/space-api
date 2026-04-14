from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_main():
    """Verifica che l'endpoint root funzioni"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "online"

def test_calculate_orbit_iss():
    """Verifica il calcolo per l'altitudine della ISS (400km)"""
    response = client.post("/calculate", json={"altitude_km": 400})
    assert response.status_code == 200
    data = response.json()
    # Il periodo per la ISS è circa 92.5 minuti
    assert 92 <= data["orbital_period_minutes"] <= 93
    assert data["velocity_km_s"] > 7.0

def test_negative_altitude():
    """Verifica che l'API rifiuti altitudini negative (Validazione Pydantic)"""
    response = client.post("/calculate", json={"altitude_km": -100})
    assert response.status_code == 422 # Error: Unprocessable Entity
