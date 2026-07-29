Building the Service: Step by Step
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Initialize the FastAPI application
app = FastAPI(title="House Price Prediction API", version="1.0")
### The FastAPI() line creates your application. The title and version parameters aren't just for show, they appear in the automatic documentation that FastAPI generates.

# Load the trained model when the service starts

model = joblib.load("house_price_model.pkl")

## we need to define what kind of data our service expects to receive. This is where Pydantic comes in:
# This is called a schema
# Define what the input data should look like
class HouseFeatures(BaseModel):
    size: float
    bedrooms: int

## We also define what the response will look like:

# Define what the output data should look like
class PredictionResponse(BaseModel):
    predicted_price: float
    currency: str = "USD"
*This ensures that every prediction response has a consistent format: a predicted_price field with the actual prediction, and a currency field that defaults to "USD"*

**Now comes the actual endpoint, the part that handles prediction requests:**

@app.post("/predict", response_model=PredictionResponse)
def predict_price(features: HouseFeatures):
    # Convert the input to the format the model expects
    X = np.array([[features.size, features.bedrooms]])

    # Make the prediction
    prediction = model.predict(X)[0]

    # Return the response
    return PredictionResponse(predicted_price=round(float(prediction), 2))

## Adding a Health Check Endpoint
@app.get("/health")
def health_check():
    return {"status": "healthy", "model_loaded": True}

## Loading Models Efficiently
*The Correct Approach: Load Once, Use Many Times*
from fastapi import FastAPI
import joblib

app = FastAPI()

*# Load the model ONCE when the application starts*
model = joblib.load("house_price_model.joblib")

@app.post("/predict")
def predict(data: dict):
    *# Use the already-loaded model*
    prediction = model.predict([data["features"]])
    return {"prediction": prediction.tolist()}

**Serving Multiple Models**
from fastapi import FastAPI
import joblib

app = FastAPI()

*# Load all models at startup into a dictionary*
models = {
    "house_price": joblib.load("house_price_model.joblib"),
    "rental_price": joblib.load("rental_price_model.joblib"),
    "property_type": joblib.load("property_classifier.joblib")
}

@app.post("/predict/{model_name}")
def predict(model_name: str, data: dict):
*# Check if the requested model exists*
    if model_name not in models:
        return {"error": f"Model '{model_name}' not found"}
    
*# Use the requested model*
    model = models[model_name]
    prediction = model.predict([data["features"]])
    return {"prediction": prediction.tolist()}

**When You Have Many Large Models: Lazy Loading**
*Lazy loading means you don't load a model until someone actually requests it.*
from fastapi import FastAPI
import joblib

app = FastAPI()

*# Start with an empty dictionary*
models = {}

def get_model(model_name: str):
*# Check if we've already loaded this model*
    if model_name not in models:
    *# This is the first request for this model, so load it*
        try:
            models[model_name] = joblib.load(f"{model_name}.joblib")
        except FileNotFoundError:
            return None
    
*# Return the model (either just loaded or already in memory)*
    return models[model_name]

@app.post("/predict/{model_name}")
def predict(model_name: str, data: dict):
    model = get_model(model_name)
    
    if model is None:
        return {"error": f"Model '{model_name}' not found"}
    
    prediction = model.predict([data["features"]])
    return {"prediction": prediction.tolist()}

**Using FastAPI's Startup Events**
from fastapi import FastAPI
import joblib

app = FastAPI()

*# Declare a global variable that will hold the model*
model = None

@app.on_event("startup")
def load_model():
    global model
    print("Loading model...")
    model = joblib.load("house_price_model.joblib")
    print("Model loaded and ready!")

@app.post("/predict")
def predict(data: dict):
    prediction = model.predict([data["features"]])
    return {"prediction": prediction.tolist()}