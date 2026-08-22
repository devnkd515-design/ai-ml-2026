# DAY 2 — Python Mental Model + Variables + Data Types
# Date: 22 August 2026

print("\n========== 1. VARIABLES AND DATA TYPES ==========")

name = "Devanshu"
age = 22
height = 5.11
learning = True
result = None

print(f"My name is {name}")
print(f"My age is {age}")
print(f"My height is {height}")
print(f"My learning is {learning}")
print(f"My result is {result}")

print(type(name))
print(type(age))
print(type(height))
print(type(learning))
print(type(result))


print("\n========== 2. TYPE CONVERSION ==========")

number_string = "25"
decimal_string = "25.5"
number = 100

number_int = int(number_string)
decimal_float = float(decimal_string)
number_string_again = str(number)

print(number_int)
print(type(number_int))

print(decimal_float)
print(type(decimal_float))

print(number_string_again)
print(type(number_string_again))

print(bool(0))
print(bool(1))
print(bool(""))
print(bool("Python"))
print(bool(None))


print("\n========== 3. OPERATORS ==========")

a = 10
b = 3

# Arithmetic
print("Arithmetic:")
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)

# Comparison
print("\nComparison:")
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)
print(a == b)
print(a != b)

# Logical
print("\nLogical:")
print(a > b and a < 20)
print(a < b or a > 5)
print(not (a < b))

# Assignment
print("\nAssignment:")
x = 10
x += 5
print(x)

x -= 2
print(x)

x *= 2
print(x)

x /= 2
print(x)

x %= 3
print(x)

# Membership
print("\nMembership:")
language = "Python"
print("P" in language)
print("z" in language)
print("z" not in language)
print("python" in language)


print("\n========== 4. INPUT AND OUTPUT ==========")

# Example input/output
user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))

print("Hello", user_name)
print("Your age is", user_age)


print("\n========== 5. F-STRINGS ==========")

goal = "AI/ML Engineer"

print(f"My name is {user_name}")
print(f"I am {user_age} years old")
print(f"My goal is {goal}")

print(f"Next year I will be {user_age + 1} years old")


print("\n========== 6. TRUTHINESS ==========")

print(bool(0))
print(bool(1))
print(bool(""))
print(bool("Hello"))
print(bool(None))
print(bool([]))


print("\n========== 7. OUTPUT PREDICTION DRILLS ==========")

x = 10
y = 3

print(x + y)
print(x / y)
print(x // y)
print(x % y)

a = 10
b = 20

print(a > b)
print(a == b)
print(a != b)

print(a and b)
print(a or b)
print(not a)


print("\n========== 8. MINI PROJECTS ==========")

# ---------- Student Report ----------

student_name = "Devanshu"
student_age = 22
student_marks = 89.80
student_attendance = 80

print("\n----- STUDENT REPORT -----")
print(f"Name: {student_name}")
print(f"Age: {student_age}")
print(f"Marks: {student_marks}")
print(f"Attendance: {student_attendance}%")
print("--------------------------")


# ---------- Celsius to Fahrenheit ----------

celsius = 25
fahrenheit = (celsius * 9 / 5) + 32

print("\nTemperature Conversion:")
print(f"{celsius}°C = {fahrenheit}°F")


# ---------- Fahrenheit to Celsius ----------

fahrenheit = 98.6
celsius = (fahrenheit - 32) * 5 / 9

print(f"{fahrenheit}°F = {celsius}°C")


# ---------- Simple Calculator ----------

first_number = 20
second_number = 5

addition = first_number + second_number
subtraction = first_number - second_number
multiplication = first_number * second_number
division = first_number / second_number

print("\n----- CALCULATOR -----")
print(f"{first_number} + {second_number} = {addition}")
print(f"{first_number} - {second_number} = {subtraction}")
print(f"{first_number} * {second_number} = {multiplication}")
print(f"{first_number} / {second_number} = {division}")
print("---------------------")


print("\n========== DAY 2 COMPLETE ==========")