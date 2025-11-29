from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import joblib
import pandas as pd
from features import build_features

app = FastAPI(title="House Price Predictor")

app.mount("/static", StaticFiles(directory="static"), name="static")

model = joblib.load("model.pkl")

@app.get("/")
def home():
    return FileResponse("static/index.html")

@app.post("/predict")
def predict(
    income: float,
    age: float,
    rooms: float,
    bedrooms: float,
    population: float
):
    df = pd.DataFrame([{
        "Avg. Area Income": income,
        "Avg. Area House Age": age,
        "Avg. Area Number of Rooms": rooms,
        "Avg. Area Number of Bedrooms": bedrooms,
        "Area Population": population
    }])

    X = build_features(df)
    pred = model.predict(X)[0]

    return {"predicted_price": float(pred)}
