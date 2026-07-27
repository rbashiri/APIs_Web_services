# File 2: main.py (uses the function from File 1)
from fastapi import FastAPI # Imports the FastAPI tool.
from helpers import greet_user
app = FastAPI()
@ app.get('/greeting')
def greeting():
    return {"message":greet_user('Alice') }
#
@app.get("/")
def home():
    return {"message": "Home page"}
from fastapi import FastAPI
from helpers import greet_user

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Home page"}

@app.get("/greeting")
def greeting():
    return {"message": greet_user("Alice")}