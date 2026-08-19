import json
try:
    with open("students.json","r") as file:
        students=json.load(file)
except FileNotFoundError:
    students = []
def save_students():
    with open("students.json","w") as file:
        json.dump(students,file,indent=4)

def add_student():
    print("\n--- Add Student ---")

    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    course = input("Enter student course: ")

    student = {
        "name": name,
        "age": age,
        "course": course
    }

    students.append(student)
    save_students()
    print("Student added successfully!")


def view_students():
    print("\n--- Student List ---")

    if len(students) == 0:
        print("No students found.")
    else:
        for i, student in enumerate(students, start=1):
            print("\nStudent", i)
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Course:", student["course"])


def search_student():
    print("\n--- Search Student ---")

    name = input("Enter student name to search: ")

    found = False

    for student in students:
        if student["name"].lower() == name.lower():
            print("\nStudent found!")
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Course:", student["course"])
            found = True

    if not found:
        print("Student not found.")


def update_student():
    print("\n--- Update Student ---")

    name = input("Enter student name to update: ")

    for student in students:
        if student["name"].lower() == name.lower():

            student["age"] = int(input("Enter new age: "))
            student["course"] = input("Enter new course: ")
            save_students()
            print("Student updated successfully!")
            return

    print("Student not found.")


def delete_student():
    print("\n--- Delete Student ---")

    name = input("Enter student name to delete: ")

    for student in students:
        if student["name"].lower() == name.lower():

            students.remove(student)
            save_students()
            print("Student deleted successfully!")
            return

    print("Student not found.")


while True:

    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("Thank you for using Student Management System!")
        break

    else:
        print("Invalid choice. Please try again.")