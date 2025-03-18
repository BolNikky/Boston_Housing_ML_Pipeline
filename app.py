from fastapi import FastAPI
import pickle
import numpy as np
from pydantic import BaseModel
 
# Load the trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)
 
# Initialize FastAPI app
app = FastAPI()
 
# Define the request body model
class PredictionInput(BaseModel):
    features: list[float]
 
# Define root endpoint
@app.get("/")
def home():
    return {"message": "Boston Housing Price Prediction API"}
 
# Define prediction endpoint
@app.post("/predict")
def predict(data: PredictionInput):
    try:
        input_data = np.array(data.features).reshape(1, -1)
        prediction = model.predict(input_data)
        return {"prediction": prediction.tolist()}
    except Exception as e:
        return {"error": str(e)}