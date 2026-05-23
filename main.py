
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello Akash! FastAPI chal raha hai"}

@app.get("/student")
def student():
    return{"name": "Rahul", "class": "12th", "city": "Delhi" }
