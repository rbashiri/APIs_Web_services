# main.py — Brings everything together
# This file imports everything and creates the FastAPI app

from fastapi import FastAPI
from api import create_user
from schemas import User

app = FastAPI()


@app.get("/health")
def health_check():
    return {"status": "ok"}
@app.post('/user')
def create_user_endpoint(user_data: User):
    return create_user(user_data)
# Start the API server from main.py:
# uvicorn main:app --reload

# Then open in browser:
# http://127.0.0.1:8000/docs
