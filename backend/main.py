# backend/main.py
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi.openapi.utils import get_openapi
import joblib
import numpy as np
import pandas as pd
import os

app = FastAPI(
    title="MVP-4 API",
    description="API para predi\u00e7\u00e3o de doen\u00e7a card\u00edaca",
    version="1.0.0",
)


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title=app.title,
        version=app.version,
        description=app.description,
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi

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
        input_df = pd.DataFrame([
            {
                "Age": data.Age,
                "RestingBP": data.RestingBP,
                "Cholesterol": data.Cholesterol,
                "FastingBS": data.FastingBS,
                "MaxHR": data.MaxHR,
                "Oldpeak": data.Oldpeak,
                "Sex": data.Sex,
                "ChestPainType": data.ChestPainType,
                "RestingECG": data.RestingECG,
                "ExerciseAngina": data.ExerciseAngina,
                "ST_Slope": data.ST_Slope,
            }
        ])

        # Faz a predição
        prediction = model.predict(input_df)[0]
        return {"prediction": int(prediction)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
