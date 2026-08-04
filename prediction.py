from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
import pandas as pd
import numpy as np
import joblib
import os
import json

router = APIRouter()

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(
            os.path.dirname(os.path.abspath(__file__))
        )
    )
)

MODEL_PATH = os.path.join(BASE_DIR, "models", "house_price.pkl")
LOCATIONS_PATH = os.path.join(BASE_DIR, "models", "locations.json")


try:
    model = joblib.load(MODEL_PATH)
except Exception as e:
    print("Model loading error:", e)
    model = None


try:
    with open(LOCATIONS_PATH, "r", encoding="utf-8") as f:
        valid_locations = json.load(f)
except Exception:
    valid_locations = []


class HouseInput(BaseModel):
    location: str
    Carpet_Area_Num: float = Field(alias="Carpet Area Num")
    Bathroom: float
    Balcony: float
    Floor: float
    Furnishing: str
    Transaction: str
    Ownership: str
    facing: str

    class Config:
        populate_by_name = True


@router.get("/locations")
def get_locations():
    return {
        "locations": valid_locations
    }


@router.post("/predict")
def predict_price(data: HouseInput):

    if model is None:
        raise HTTPException(
            status_code=500,
            detail="Model not loaded"
        )

    try:

        input_data = pd.DataFrame([{
            "location_grouped": data.location,
            "Carpet Area Num": data.Carpet_Area_Num,
            "Bathroom": data.Bathroom,
            "Balcony": data.Balcony,
            "Floor": data.Floor,
            "Furnishing": data.Furnishing,
            "Transaction": data.Transaction,
            "Ownership": data.Ownership,
            "facing": data.facing
        }])

        print(input_data)
        print(input_data.columns.tolist())
        prediction_log = model.predict(input_data)[0]
        prediction_price = np.expm1(prediction_log)
    
        print(prediction_log)

        if not np.isfinite(prediction_price):
          raise HTTPException(
          status_code=400,
          detail="Prediction value is invalid. Check input values."
    ) 
        

        return {
            "success": True,
            "predicted_price": round(float(prediction_price), 2)
            
        }


    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Prediction error: {str(e)}"
        )