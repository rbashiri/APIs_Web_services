# Step 1: Create main.py
from fastapi import FastAPI # Imports the FastAPI tool.

app = FastAPI() # Creates your API application and names it app.
# Creates a GET endpoint.
# The / means the main or home address:

# Step3: Start the API :uvicorn main:app --reload
#Each part has a meaning:
#uvicorn → starts the server
#main → looks for main.py
#pp → looks for the variable named app
# --reload → restarts automatically when you change the code.
@app.get("/")

def hello():
    return {"message": "Hello World"}
@app.get("/students")
def get_students():
    return {
        "students": ["Sara", "Ali", "John"]}

# Start the API server from main.py:
# uvicorn main:app --reload

# Then open in browser:
# http://127.0.0.1:8000/docs

# Or test from terminal:
# curl http://127.0.0.1:8000/
# Open http://127.0.0.1:8000/docs for Swagger UI.
# Add another route like /health to practice multiple endpoints.
@app.get("/Birthday")
def get_baby():
    return{"Birthday": "Happy Birthday suasan and I love you!!!!!"}
@app.get('/root')
def read_root():
    return {'root': 'I am not sure about it'}

# Creating API Endpoints with PUT Request:
# 
# An endpoint is a specific address in an API where you send a request to perform an action.
app= FastAPI()
@ app.get('/')
def read_root():
    return{'Hello': 'FastAPI'}


# New PUT endpoint
# New PUT endpoint
@app.put('/user/{user_id}')
def update_user(user_id: int, name: str, age: int):
    return {
        "user_id": user_id,
        "name": name,
        "age": age,
        "message": f"User {user_id} has been updated"}


