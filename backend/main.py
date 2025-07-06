# backend/main.py
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import numpy as np
import os

app = FastAPI()

# Permite que aplicações front-end em outros domínios/acessos consumam a API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Carrega o modelo treinado
# O caminho relativo depende de onde o servidor é iniciado, então
# calculamos o caminho absoluto baseado neste arquivo.
MODEL_PATH = os.path.join(os.path.dirname(__file__), "melhor_modelo.pkl")
model = joblib.load(MODEL_PATH)

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
