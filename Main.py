from fastapi import FastAPI
from pydantic import BaseModel
from model_logic import FifaValuePredictor
from contextlib import asynccontextmanager

predictor = FifaValuePredictor()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # تحميل الموديل عند البداية من فولدر assets
    predictor.load_assets(path="assets/fifa")
    yield

app = FastAPI(title="FIFA Prediction API", lifespan=lifespan)

class PlayerData(BaseModel):
    features: list[float]

@app.get("/")
def home():
    return {"message": "FIFA API is Online"}

@app.post("/predict")
async def predict(data: PlayerData):
    result = predictor.predict(data.features)
    return {"predicted_value": float(result[0][0]), "unit": "Euro"}