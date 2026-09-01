import sys
import os

sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "src")
    )
)

from models import Student
from analyzer import (
    calculate_class_average,
    highest_performer,
    lowest_performer,
    calculate_attendance_average,
    search_student,
    pass_fail_statistics
)

students = [
    Student(101, "Devanshu", [85, 95, 90], 90),
    Student(102, "Rahul", [70, 75, 80], 85),
    Student(103, "Aman", [95, 95, 100], 95),
    Student(104, "Neha", [30, 35, 40], 70)
]


# Class average

assert abs(calculate_class_average(students) - 74.16666666666667) < 0.001


# Highest performer

highest = highest_performer(students)

assert highest.name == "Aman"


# Lowest performer

lowest = lowest_performer(students)

assert lowest.name == "Neha"


# Attendance average

assert calculate_attendance_average(students) == 85


# Search by name

results = search_student(students, "Devanshu")

assert len(results) == 1
assert results[0].name == "Devanshu"


# Search by ID

results = search_student(students, "102")

assert len(results) == 1
assert results[0].name == "Rahul"


# Pass/fail

statistics = pass_fail_statistics(students)

assert statistics["passed"] == 3
assert statistics["failed"] == 1


print("All tests passed.")