from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      # يسمح من أي مصدر (للتجربة فقط)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Student(BaseModel):
    id: int
    name: str
    grade: int

Students = [
    Student(id=1,name="jafar aqraa",grade=5),
    Student(id=2,name="jood aqraa",grade=1),

]

@app.get("/student/")
def read_student():
    return Students



@app.post("/student/")
def create_student(New_student: Student):
    Students.append(New_student)
    return New_student


@app.put("/student/{student_id}")
def update_student(student_id: int, updated_student: Student):
    for index, Student in enumerate(Students):
        if Student.id == student_id:
            Students[index] = updated_student
            return update_student
    return {"error": "student not found"}    

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    for index, student in enumerate(Students):
        if student.id == student_id:
            del Students[index]
    return {"message": "Student deleted successfully"}
