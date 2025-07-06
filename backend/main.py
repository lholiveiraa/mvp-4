# backend/main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

# Carrega o modelo treinado
model = joblib.load("melhor_modelo.pkl")

# Define o schema dos dados esperados (exemplo simplificado)
class PatientData(BaseModel):
    Age: int
    RestingBP: int
    Cholesterol: int
    FastingBS: int
    MaxHR: int
    Oldpeak: float
    Sex: str
    ChestPainType: str
    RestingECG: str
    ExerciseAngina: str
    ST_Slope: str

@app.post("/predict")
def predict(data: PatientData):
    try:
        # Organiza os dados na mesma ordem usada no treino
        input_data = [[
            data.Age, data.RestingBP, data.Cholesterol, data.FastingBS,
            data.MaxHR, data.Oldpeak, data.Sex, data.ChestPainType,
            data.RestingECG, data.ExerciseAngina, data.ST_Slope
        ]]

        # Faz a predição
        prediction = model.predict(input_data)[0]
        return {"prediction": int(prediction)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))