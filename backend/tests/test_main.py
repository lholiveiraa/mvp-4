from fastapi.testclient import TestClient
import sys
from pathlib import Path

# Garantir que o diretório raiz esteja no caminho de importação
ROOT_DIR = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT_DIR))

from backend.main import app

client = TestClient(app)


def test_predict_endpoint():
    sample_data = {
        "Age": 40,
        "RestingBP": 120,
        "Cholesterol": 200,
        "FastingBS": 0,
        "MaxHR": 150,
        "Oldpeak": 1.0,
        "Sex": "M",
        "ChestPainType": "ATA",
        "RestingECG": "Normal",
        "ExerciseAngina": "N",
        "ST_Slope": "Up",
    }
    response = client.post("/predict", json=sample_data)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert "prediction" in data
    assert isinstance(data["prediction"], int)
