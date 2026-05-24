students = [
    {"id": 1, "name": "Rahul", "city": "Delhi"},
    {"id": 2, "name": "Priya", "city": "Mumbai"},
    {"id": 3, "name": "Akash", "city": "Delhi"}
]

from fastapi import FastAPI

app = FastAPI()

@app.get("/")

def home():
    return{"message": "Hello Akash Raghuwanshi Your FastAPI is working properly"}


@app.get("/student")
def get_student():
    return students


@app.post("/student")

#def add_student(data: dict):
 #   name = data["name"]
  #  city = data["city"]
   # return {
    #    "message": f"{name} from {city} added successfully!", "student" : data
def add_student(data: dict):
    students.append(data)
    return {
        "message": f"Student added successfully!",
        "student": data
    }
    }

# PATCH
@app.patch("/student/{student_id}")
def update_student(student_id: int, data: dict):
    for student in students:
        if student["id"] == student_id:
            student.update(data)
            return {
                "message": f"Student {student_id} updated successfully!",
                "updated student": student
            }
    return {"message": "Student not found!"}


#delete
@app.delete("/student/{student_id}")
def delete_student(student_id: int):
    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            return {
                "message": f"Student {student_id} deleted successfully!"
            }
    return {"message": "Student not found!"}