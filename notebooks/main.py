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

# Open http://127.0.0.1:8000/docs for Swagger UI.
# Add another route like /health to practice multiple endpoints.
@app.get("/Birthday")
def get_students():
    return{"Birthday": "Happy Birthday suasan and I love you!!!!!"}