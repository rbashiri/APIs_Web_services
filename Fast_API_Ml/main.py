# main.py
from fastapi import FastAPI
from api import create_user, get_user, update_user, list_users
from schemas import UserCreats, UserUpdate

# Create the FastAPI application
app = FastAPI()

@app.get('/users')
def get_all_users():
    """Endpoint to get all users"""
    return list_users()

@app.get('/user/{user_id}')
def get_user_endpoint(user_id: int):
    """Endpoint to get a specific user"""
    return get_user(user_id)

@app.post('/user')
def create_user_endpoint(user_data: UserCreats):
    """Endpoint to create a new user"""
    return create_user(user_data)

@app.put('/user/{user_id}')
def update_user_endpoint(user_id: int, user_data: UserUpdate):
    """Endpoint to update a user"""
    return update_user(user_id, user_data)