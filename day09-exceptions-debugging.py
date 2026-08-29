# DAY 9 — EXCEPTIONS + DEBUGGING + CODE QUALITY
# Date: 29 August 2026


import logging


# ============================================================
# BASIC LOGGING SETUP
# ============================================================

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)


# ============================================================
# 1. try / except
# ============================================================

def divide_numbers(a, b):

    try:
        result = a / b
        return result

    except ZeroDivisionError:
        return "Cannot divide by zero."


print(divide_numbers(10, 2))
print(divide_numbers(10, 0))


# ============================================================
# 2. try / except / else / finally
# ============================================================

def convert_number(value):

    try:
        number = int(value)

    except ValueError:
        print("Invalid integer.")

    else:
        print(f"Conversion successful: {number}")

    finally:
        print("Conversion attempt finished.")


convert_number("25")
convert_number("hello")


# ============================================================
# 3. RAISING EXCEPTIONS
# ============================================================

def check_age(age):

    if age < 0:
        raise ValueError("Age cannot be negative.")

    return age


print(check_age(22))


# Test separately:
#
# print(check_age(-5))


# ============================================================
# 4. ASSERTIONS
# ============================================================

def calculate_average(numbers):

    assert len(numbers) > 0, "List cannot be empty."

    return sum(numbers) / len(numbers)


print(calculate_average([10, 20, 30]))


# ============================================================
# 5. BASIC LOGGING
# ============================================================

def process_data(data):

    logging.info("Starting data processing.")

    if not data:
        logging.warning("Received empty data.")
        return

    logging.info(f"Processing {len(data)} items.")

    logging.info("Data processing completed.")


process_data([10, 20, 30])
process_data([])


# ============================================================
# 6. READABLE FUNCTION DESIGN
# ============================================================

def calculate_mean(numbers):

    if not numbers:
        raise ValueError("Numbers list cannot be empty.")

    total = sum(numbers)

    return total / len(numbers)


def calculate_grade(average):

    if average >= 90:
        return "A"

    elif average >= 80:
        return "B"

    elif average >= 70:
        return "C"

    elif average >= 60:
        return "D"

    return "F"


marks = [85, 92, 78, 90]

average = calculate_mean(marks)

grade = calculate_grade(average)

print(f"Average: {average}")
print(f"Grade: {grade}")


# ============================================================
# 7. PEP 8 / NAMING EXAMPLES
# ============================================================

student_name = "Devanshu"
student_age = 22
student_marks = [85, 90, 78]

print(student_name)
print(student_age)
print(student_marks)


# ============================================================
# 8. DEBUGGING PRACTICE
# ============================================================

# The following intentionally broken examples are kept
# commented so the main file can execute successfully.


# BUG 1 — NameError
#
# print(student)


# BUG 2 — TypeError
#
# age = 22
# print(age + " years")


# BUG 3 — IndexError
#
# numbers = [10, 20, 30]
# print(numbers[5])


# BUG 4 — KeyError
#
# student = {"name": "Devanshu"}
# print(student["age"])


# BUG 5 — ZeroDivisionError
#
# a = 10
# b = 0
# print(a / b)


# ============================================================
# 9. == VS is
# ============================================================

a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
print(a is b)


# ============================================================
# 10. MUTABILITY
# ============================================================

numbers = [1, 2, 3]

numbers.append(4)

print(numbers)


# ============================================================
# 11. FINAL CHECK
# ============================================================

print("DAY 9 COMPLETE")