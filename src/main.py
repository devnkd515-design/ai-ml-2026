import json
import os

from models import Student
from analyzer import (
    calculate_class_average,
    highest_performer,
    lowest_performer,
    calculate_attendance_average,
    search_student,
    pass_fail_statistics
)


DATA_FILE = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "data",
    "students.json"
)


def load_students():
    try:
        with open(DATA_FILE, "r") as file:
            data = json.load(file)

        students = []

        for item in data:
            student = Student(
                item["id"],
                item["name"],
                item["marks"],
                item["attendance"]
            )

            students.append(student)

        return students

    except FileNotFoundError:
        print("Student data file not found.")
        return []

    except json.JSONDecodeError:
        print("Invalid JSON data.")
        return []

    except KeyError:
        print("Student record has missing fields.")
        return []


def show_students(students):
    if not students:
        print("No students found.")
        return

    print("\n===== STUDENTS =====")

    for student in students:
        print(student)


def show_class_average(students):
    average = calculate_class_average(students)

    print(f"\nClass Average: {average:.2f}")


def show_highest(students):
    student = highest_performer(students)

    if student is None:
        print("No students found.")
        return

    print("\n===== HIGHEST PERFORMER =====")
    print(student)


def show_lowest(students):
    student = lowest_performer(students)

    if student is None:
        print("No students found.")
        return

    print("\n===== LOWEST PERFORMER =====")
    print(student)


def show_pass_fail(students):
    statistics = pass_fail_statistics(students)

    print("\n===== PASS / FAIL =====")
    print(f"Passed: {statistics['passed']}")
    print(f"Failed: {statistics['failed']}")


def show_attendance(students):
    average = calculate_attendance_average(students)

    print(f"\nAverage Attendance: {average:.2f}%")


def find_student(students):
    query = input("Enter student name or ID: ")

    results = search_student(students, query)

    if not results:
        print("Student not found.")
        return

    print("\n===== SEARCH RESULTS =====")

    for student in results:
        print(student)


def main():
    students = load_students()

    while True:

        print("\n===== STUDENT PERFORMANCE ANALYZER =====")
        print("1. Show all students")
        print("2. Class average")
        print("3. Highest performer")
        print("4. Lowest performer")
        print("5. Pass/fail statistics")
        print("6. Attendance statistics")
        print("7. Search student")
        print("8. Exit")

        choice = input("Enter choice: ")

        try:

            if choice == "1":
                show_students(students)

            elif choice == "2":
                show_class_average(students)

            elif choice == "3":
                show_highest(students)

            elif choice == "4":
                show_lowest(students)

            elif choice == "5":
                show_pass_fail(students)

            elif choice == "6":
                show_attendance(students)

            elif choice == "7":
                find_student(students)

            elif choice == "8":
                print("Program closed.")
                break

            else:
                print("Invalid choice.")

        except Exception as error:
            print(f"Unexpected error: {error}")


if __name__ == "__main__":
    main()