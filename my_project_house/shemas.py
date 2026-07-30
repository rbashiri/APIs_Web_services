# schemas.py :each class describes the shape of the data your API will return. 
# Think of it as a form: every field has a name and an expected data type.
from pydantic import BaseModel, Field
from typing import Optional

# Create a class  with name of predicitionResponse
class PredictionResponse(BaseModel):
    predicted_price : float
    currency: str
    model_version: str

class ModelInfoResponse(BaseModel):
    model_type:str
    version:str
    features:list[str]
    training_date:str
    rmse:float
    descrpition: str
class HealthCheckResponse(BaseModel):
    status:str
    model_loaded:bool # accepts only True or False.
    message: str
