# main.py
from fastapi import FastAPI
# Import the functions from api.py
from api import get_user, update_user , list_users #  import the three functions from api.py
# Create the FastAPI application
app = FastAPI()
# line 9-12 : create a GET endpoint at /users that calls list_users()
# Connect the imported functions to actual API endpoints
@app.get('/users')
def get_all_users():
    """Endpoint to get all users"""
    return list_users()
# lines 14-17 : create a GET endpoint at /user/{user_id} that calls get_user()
@app.get('/user/{user_id}')
def get_user_endpoint(user_id :int):
    """Endpoint to get specific user"""
    return get_user(user_id)
# lines 19-22 : create a put endpoint at /user/{user_id} that calls update_user()
@app.put('/user/{user_id}')
def update_user_endpoint(user_id: int, name: str, email: str):
    """Endpoint to update a user"""
    return update_user(user_id, name, email)
# Start the API server from main.py:
# uvicorn main:app --reload

# Then open in browser:
# http://127.0.0.1:8000/docs
@app.get("/health")
def health():
    return {"status": "ok"}