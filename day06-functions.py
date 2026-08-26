# DAY 6 — FUNCTIONS + COMPREHENSIONS
# Date: 26 August 2026


# ============================================================
# 1. BASIC FUNCTION
# ============================================================

def square(x):
    return x * x


result = square(5)

print(result)


# ============================================================
# 2. PRINT VS RETURN
# ============================================================

def print_square(x):
    print(x * x)


def return_square(x):
    return x * x


print_square(5)

result = return_square(5)

print(result)


# ============================================================
# 3. PARAMETERS AND ARGUMENTS
# ============================================================

def add(a, b):
    return a + b


result = add(10, 20)

print(result)


# ============================================================
# 4. MULTIPLE RETURN VALUES
# ============================================================

def calculate(a, b):

    total = a + b
    difference = a - b

    return total, difference


total, difference = calculate(10, 3)

print(total)
print(difference)


# ============================================================
# 5. POSITIONAL ARGUMENTS
# ============================================================

def greet(name, age):
    return f"{name} is {age} years old"


print(greet("Devanshu", 22))


# ============================================================
# 6. KEYWORD ARGUMENTS
# ============================================================

print(greet(age=22, name="Devanshu"))


# ============================================================
# 7. DEFAULT ARGUMENTS
# ============================================================

def welcome(name, country="India"):
    return f"{name} is from {country}"


print(welcome("Devanshu"))

print(welcome("Devanshu", "USA"))


# ============================================================
# 8. *args
# ============================================================

def total(*args):

    result = 0

    for number in args:
        result += number

    return result


print(total(10, 20, 30))

print(total(1, 2, 3, 4, 5))

print(total())


# ============================================================
# 9. **kwargs
# ============================================================

def profile(**kwargs):

    print(kwargs)


profile(
    name="Devanshu",
    age=22,
    branch="CSE"
)

profile(
    city="Pune"
)

profile()


# ============================================================
# 10. *args + **kwargs
# ============================================================

def test(*args, **kwargs):

    return args, kwargs


result = test(
    1,
    2,
    3,
    name="Dev",
    city="Pune"
)

print(result)


# ============================================================
# 11. SCOPE
# ============================================================

x = 10


def scope_test():

    x = 20

    return x


print(scope_test())

print(x)


# ============================================================
# 12. GLOBAL VARIABLE
# ============================================================

x = 10


def change_global():

    global x

    x = 20


change_global()

print(x)


# ============================================================
# 13. LAMBDA
# ============================================================

square = lambda x: x * x

print(square(5))


add = lambda a, b: a + b

print(add(3, 7))


# ============================================================
# 14. LAMBDA WITH SORT
# ============================================================

students = [
    ("Dev", 85),
    ("Rahul", 92),
    ("Aman", 78)
]

students.sort(key=lambda student: student[1])

print(students)


# ============================================================
# 15. LIST COMPREHENSION — TRANSFORM
# ============================================================

numbers = [1, 2, 3, 4, 5]

squares = [
    x * x
    for x in numbers
]

print(squares)


# ============================================================
# 16. LIST COMPREHENSION — FILTER
# ============================================================

even_numbers = [
    x
    for x in numbers
    if x % 2 == 0
]

print(even_numbers)


# ============================================================
# 17. LIST COMPREHENSION — FILTER + TRANSFORM
# ============================================================

even_squares = [
    x * x
    for x in numbers
    if x % 2 == 0
]

print(even_squares)


# ============================================================
# 18. DICTIONARY COMPREHENSION
# ============================================================

squares_dict = {
    x: x * x
    for x in numbers
}

print(squares_dict)


# ============================================================
# 19. DICTIONARY COMPREHENSION WITH FILTER
# ============================================================

even_dict = {
    x: x * x
    for x in numbers
    if x % 2 == 0
}

print(even_dict)


# ============================================================
# 20. SET COMPREHENSION
# ============================================================

even_set = {
    x * 2
    for x in numbers
    if x % 2 == 0
}

print(even_set)


# ============================================================
# 21. DRILL — MEAN
# ============================================================

def calculate_mean(numbers):

    total = 0
    count = 0

    for number in numbers:

        total += number
        count += 1

    return total / count


numbers = [10, 20, 30, 40]

print(calculate_mean(numbers))


# ============================================================
# 22. DRILL — MAX
# ============================================================

def find_max(numbers):

    largest = numbers[0]

    for number in numbers:

        if number > largest:
            largest = number

    return largest


numbers = [10, 45, 23, 67, 12]

print(find_max(numbers))


# ============================================================
# 23. DRILL — MIN
# ============================================================

def find_min(numbers):

    smallest = numbers[0]

    for number in numbers:

        if number < smallest:
            smallest = number

    return smallest


numbers = [10, 45, 23, 67, 12]

print(find_min(numbers))


# ============================================================
# 24. DRILL — GRADE CALCULATION
# ============================================================

def calculate_grade(marks):

    if marks >= 90:
        return "A"

    elif marks >= 80:
        return "B"

    elif marks >= 70:
        return "C"

    elif marks >= 60:
        return "D"

    else:
        return "F"


print(calculate_grade(92))
print(calculate_grade(75))
print(calculate_grade(50))


# ============================================================
# 25. DRILL — INPUT VALIDATION
# ============================================================

def get_number():

    while True:

        value = input("Enter a number: ")

        try:

            number = int(value)

            return number

        except ValueError:

            print("Invalid number. Try again.")


# Test:
#
# number = get_number()
# print(f"You entered: {number}")


# ============================================================
# 26. INPUT VALIDATION — POSITIVE NUMBER
# ============================================================

def get_positive_number():

    while True:

        value = input("Enter a positive number: ")

        try:

            number = int(value)

            if number > 0:
                return number

            else:
                print("Number must be positive.")

        except ValueError:

            print("Invalid number.")


# Test:
#
# number = get_positive_number()
# print(number)


# ============================================================
# 27. REFACTOR — FACTORIAL
# ============================================================

def factorial(n):

    fact = 1

    for i in range(1, n + 1):

        fact *= i

    return fact


print(factorial(5))


# ============================================================
# 28. REFACTOR — FIBONACCI
# ============================================================

def fibonacci(n):

    first = 0
    second = 1

    result = []

    for i in range(n):

        result.append(first)

        next_number = first + second

        first = second
        second = next_number

    return result


print(fibonacci(10))


# ============================================================
# 29. REFACTOR — PRIME CHECK
# ============================================================

def is_prime(n):

    if n <= 1:
        return False

    for i in range(2, n):

        if n % i == 0:
            return False

    return True


print(is_prime(13))
print(is_prime(15))


# ============================================================
# 30. REFACTOR — PALINDROME
# ============================================================

def is_palindrome(text):

    reverse = ""

    for i in range(len(text) - 1, -1, -1):

        reverse += text[i]

    return text == reverse


print(is_palindrome("madam"))
print(is_palindrome("python"))


# ============================================================
# 31. REFACTOR — VOWEL COUNT
# ============================================================

def count_vowels(text):

    vowels = "aeiouAEIOU"

    count = 0

    for character in text:

        if character in vowels:
            count += 1

    return count


print(count_vowels("hello python"))


# ============================================================
# 32. FUNCTION DESIGN — ONE CLEAR RESPONSIBILITY
# ============================================================

def calculate_average(marks):

    total = 0
    count = 0

    for mark in marks:

        total += mark
        count += 1

    return total / count


def calculate_grade_from_average(average):

    if average >= 90:
        return "A"

    elif average >= 80:
        return "B"

    elif average >= 70:
        return "C"

    elif average >= 60:
        return "D"

    else:
        return "F"


marks = [85, 90, 78]

average = calculate_average(marks)

grade = calculate_grade_from_average(average)

print(f"Average = {average}")
print(f"Grade = {grade}")


# ============================================================
# DAY 6 COMPLETE
# ============================================================

print("DAY 6 COMPLETE")