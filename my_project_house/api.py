# api.py : which contains all the business logic - the actual functions that do the work.

from pathlib import Path # Import the Path tool from Python's pathlib library
import joblib
import numpy as np
import json
from typing import Dict, Any
import os
# Find the full path of this Python file and get its folder
BASE_DIR = Path(__file__).resolve().parent
# Create the complete path to model.pkl inside that folder
MODEL_PATH = BASE_DIR / "model.pkl"
# Create the complete path to model_metadata.json inside that folder
METADATA_PATH = BASE_DIR / "model_metadata.json"

# Global variable to store the loaded model
model = None
metadata = None

#  Add code to actually load the model and metadata files
def load_model_and_metadata(): 
    """
        Load the trained model and metadata from disk.
        This function should:
         1. Load model.pkl using joblib.load()
         2. Load model_metadata.json using json.load()
         3. Store them in the global variables
         4. Return True if successful, False if there's an error
    """
    global model, model_metadata
    try:
        model =joblib.load(MODEL_PATH)
    # YOUR TASK: Load the metadata
        # Open 'model_metadata.json' and load it with json.load()
        with open(METADATA_PATH, "r", encoding="utf-8") as file: # r means read the file 
            # Gives the opened file the temporary name file.
            model_metadata = json.load(file) # Gives the opened file the temporary name file.
        print("Model and metadata loaded successfully!")
        return True
   
    except Exception as error:
        model = None
        model_metadata = None
        print(f"Error loading model and metadata: {error}")
        return False



# Extract features, convert to numpy array, and make prediction
def make_prediction(house_features: Dict[str, Any]) -> float:
    """
    Make a price prediction for one house.
    """

    # Use the model variable that was created outside this function
    global model

    # Stop the function if the trained model has not been loaded
    if model is None:
        raise ValueError("Model not loaded")

    # Get the feature values in the same order used during model training
    feature_values = [
        house_features[feature_name]
        for feature_name in model_metadata["features"]
    ]

    # Convert the feature list into a two-dimensional NumPy array
    # The result has 1 row (one house) and 13 columns (13 features)
    X = np.array([feature_values], dtype=float)

    # Ask the trained model to predict the price
    # predict() returns an array, and [0] extracts the first prediction
    prediction = model.predict(X)[0]

    # Convert the prediction to a Python float and round it to 2 decimals
    return round(float(prediction), 2)
     
    

# Return the metadata or raise an error if not loaded
def get_model_info():
    """Return information about the loaded model."""

    if model_metadata is None:
        raise RuntimeError("Model metadata has not been loaded.")

    return model_metadata



# Implement health status checks
def check_health():
    """Check whether the API has everything required for prediction."""

    model_is_loaded = model is not None
    metadata_is_loaded = model_metadata is not None

    if model_is_loaded and metadata_is_loaded:
        return {
            "status": "healthy",
            "model_loaded": True,
            "message": "The model and metadata are loaded and ready."
        }

    if not model_is_loaded:
        return {
            "status": "unhealthy",
            "model_loaded": False,
            "message": "The model is not loaded."
        }

    return {
        "status": "unhealthy",
        "model_loaded": True,
        "message": "The model is loaded, but its metadata is unavailable."
    }