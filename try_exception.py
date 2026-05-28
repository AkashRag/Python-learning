try:
    number=int("abcd" )
except Exception as e:
    print(f"Gadbad:{e}")

from fastapi import FastAPI

app = FastAPI()

students = [
    {"id": 1, "name": "Rahul", "city": "Delhi"},
    {"id": 2, "name": "Priya", "city": "Mumbai"},
    {"id": 3, "name": "Akash", "city": "Delhi"}
]


@app.delete("/student/{student_id}")
def delete_student(student_id: int):
    try:
        for student in students:
            if student["id"] == student_id:
                students.remove(student)
                return {"message": f"Student {student_id} deleted!"}
        return {"message": "Student not found!"}
    except Exception as e:
        return {"error": f"Kuch gadbad hui: {e}"}