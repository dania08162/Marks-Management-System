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
def update_student(name, marks):
    if name in student:
        student[name] = marks
        print("Marks updated successfully.")
    else:
        print("Student not found.")
def delete_student(name):
    if name in student:
        del student[name]
        print("Student deleted successfully.")
    else:
        print("Student not found.")
def main():
    while True:
        print("\nStudent Marks Management System")
        print("1. Add Student")
        print("2. View Student")
        print("3. View All Students")
        print("4. Update Student Marks")
        print("5. Delete Student")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            name = input("Enter student name: ")
            marks = input("Enter student marks: ")
            add_student(name, marks)
        elif choice == '2':
            name = input("Enter student name: ")
            view_student(name)
        elif choice == '3':
            view_all_students()
        elif choice == '4':
            name = input("Enter student name: ")
            marks = input("Enter new marks: ")
            update_student(name, marks)
        elif choice == '5':
            name = input("Enter student name: ")
            delete_student(name)
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()