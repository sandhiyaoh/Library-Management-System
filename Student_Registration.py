# Student Registration Module

students = []

def register_student(student_id, name, age, course):
    student = {
        "ID": student_id,
        "Name": name,
        "Age": age,
        "Course": course
    }
    students.append(student)
    print("Student registered successfully")

def display_students():
    if not students:
        print("No students registered")
        return

    for student in students:
        print(student)

# Sample usage
register_student(1, "Arun", 20, "Computer Science")
display_students()
