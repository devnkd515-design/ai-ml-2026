# DAY 7 — FILE HANDLING + JSON + MODULES
# Date: 27 August 2026


import json
import os


# ============================================================
# 1. FILE PATH
# ============================================================

DATA_FILE = "data.json"


# ============================================================
# 2. LOAD STUDENT DATA
# ============================================================

def load_students():

    try:
        with open(DATA_FILE, "r") as file:
            students = json.load(file)

        return students

    except FileNotFoundError:

        print("data.json not found. Creating empty student records.")

        return []

    except json.JSONDecodeError:

        print("Invalid JSON data.")

        return []


# ============================================================
# 3. SAVE STUDENT DATA
# ============================================================

def save_students(students):

    with open(DATA_FILE, "w") as file:
        json.dump(students, file, indent=4)


# ============================================================
# 4. ADD STUDENT
# ============================================================

def add_student(students):

    name = input("Enter student name: ")

    age = int(input("Enter student age: "))

    branch = input("Enter branch: ")

    marks = float(input("Enter marks: "))

    student = {
        "name": name,
        "age": age,
        "branch": branch,
        "marks": marks
    }

    students.append(student)

    save_students(students)

    print("Student added successfully.")


# ============================================================
# 5. SHOW STUDENTS
# ============================================================

def show_students(students):

    if not students:

        print("No student records found.")

        return

    for student in students:

        print("-------------------------")

        print(f"Name   : {student['name']}")
        print(f"Age    : {student['age']}")
        print(f"Branch : {student['branch']}")
        print(f"Marks  : {student['marks']}")

    print("-------------------------")


# ============================================================
# 6. FIND STUDENT
# ============================================================

def find_student(students):

    name = input("Enter student name to search: ")

    for student in students:

        if student["name"].lower() == name.lower():

            print("-------------------------")

            print(f"Name   : {student['name']}")
            print(f"Age    : {student['age']}")
            print(f"Branch : {student['branch']}")
            print(f"Marks  : {student['marks']}")

            print("-------------------------")

            return

    print("Student not found.")


# ============================================================
# 7. DELETE STUDENT
# ============================================================

def delete_student(students):

    name = input("Enter student name to delete: ")

    for student in students:

        if student["name"].lower() == name.lower():

            students.remove(student)

            save_students(students)

            print("Student deleted.")

            return

    print("Student not found.")


# ============================================================
# 8. MAIN PROGRAM
# ============================================================

def main():

    students = load_students()

    while True:

        print("\n===== STUDENT RECORD SYSTEM =====")

        print("1. Add student")
        print("2. Show students")
        print("3. Find student")
        print("4. Delete student")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":

            add_student(students)

        elif choice == "2":

            show_students(students)

        elif choice == "3":

            find_student(students)

        elif choice == "4":

            delete_student(students)

        elif choice == "5":

            print("Program exited.")

            break

        else:

            print("Invalid choice.")


# ============================================================
# PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":

    main()