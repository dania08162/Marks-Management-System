student = {}
def add_student(name, marks):
    student[name] = marks
    print("Student added successfully.")
def view_student(name):
    if name in student:
        print(f"Marks of {name}: {student[name]}")
    else:
        print("Student not found.")
def view_all_students():
    if student:
        for name, marks in student.items():
            print(f"{name}: {marks}")
    else:
        print("No students found.")
