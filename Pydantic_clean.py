from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class Student(BaseModel):
    name : str
    city : str
    age : int = Field(ge=1, le=100)

@app.post("/student")
def add_student(data: Student):
    return{
        "message": f"{data.name} added successfully!",
        "student": data
    }

