from fastapi import FastAPI

app = FastAPI()

@app.get("/")

def home():
    return{"message": "Hello Akash Raghuwanshi Your FastAPI is working properly"}


@app.get("/student")
def get_student():
    return{"name": "Rahul", "class": "12th", "city": "Delhi"}


@app.post("/student")

def add_student(data: dict):
    name = data["name"]
    city = data["city"]
    return {
        "message": f"{name} from {city} added successfully!", "student" : data
    }

# PATCH
@app.patch("/student/{student_id}")

def update_student(student_id: int, data: dict) :
    return  {
        "message": f" Student {student_id} updated successfully!", "updated data": data
    }

@app.delete("/student/{student_id}")

def student_delete(student_id: int):
    return{
        "message": f"student {student_id} deleted succssesfully"

    }