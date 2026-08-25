# DAY 5 — TUPLES + SETS + DICTIONARIES
# Date: 25 August 2026


# ============================================================
# 1. TUPLES — CREATION, INDEXING, SLICING
# ============================================================

data = ("Python", 22, True, 5.11)

print(data)
print(data[0])
print(data[2])
print(data[-1])
print(data[1:3])


# ============================================================
# 2. TUPLE IMMUTABILITY
# ============================================================

# Tuples cannot be modified after creation.

# data[1] = 23
# TypeError


# ============================================================
# 3. TUPLE UNPACKING
# ============================================================

person = ("Devanshu", 22, "Engineer")

name, age, profession = person

print(name)
print(age)
print(profession)


coordinates = (10, 20)

x, y = coordinates

print(x)
print(y)


# ============================================================
# 4. SET — CREATION AND UNIQUENESS
# ============================================================

numbers = {1, 2, 3, 3, 4, 4}

print(numbers)


# ============================================================
# 5. SET MEMBERSHIP
# ============================================================

print(3 in numbers)
print(10 in numbers)


# ============================================================
# 6. SET ADD / REMOVE / DISCARD
# ============================================================

numbers.add(5)

print(numbers)

numbers.remove(5)

print(numbers)

numbers.discard(10)

print(numbers)


# ============================================================
# 7. SET OPERATIONS
# ============================================================

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

union = A | B
intersection = A & B
difference = A - B
reverse_difference = B - A

print(f"Union = {union}")
print(f"Intersection = {intersection}")
print(f"A - B = {difference}")
print(f"B - A = {reverse_difference}")


# ============================================================
# 8. DICTIONARY — CREATION AND ACCESS
# ============================================================

student = {
    "name": "Devanshu",
    "age": 22,
    "branch": "Engineering"
}

print(student)

print(student["name"])
print(student["age"])
print(student["branch"])


# ============================================================
# 9. DICTIONARY — ADD / UPDATE
# ============================================================

student["city"] = "Pune"

student["age"] = 23

print(student)


# ============================================================
# 10. DICTIONARY — DELETE
# ============================================================

del student["city"]

print(student)


# ============================================================
# 11. DICTIONARY METHODS
# ============================================================

print(student.keys())
print(student.values())
print(student.items())

print(student.get("name"))
print(student.get("phone"))
print(student.get("phone", "Not available"))


# pop()

removed_age = student.pop("age")

print(removed_age)
print(student)


# update()

student.update({
    "age": 22,
    "city": "Pune"
})

print(student)


# ============================================================
# 12. DICTIONARY MEMBERSHIP
# ============================================================

print("name" in student)
print("Devanshu" in student)
print("Devanshu" in student.values())


# ============================================================
# 13. LOOP THROUGH DICTIONARY
# ============================================================

for key, value in student.items():
    print(key, value)


# ============================================================
# 14. NESTED DICTIONARY + LIST
# ============================================================

students = {
    "student1": {
        "name": "Devanshu",
        "age": 22,
        "marks": [85, 90, 78]
    },

    "student2": {
        "name": "Rahul",
        "age": 21,
        "marks": [75, 88, 92]
    }
}

print(students["student1"]["name"])
print(students["student1"]["marks"][0])
print(students["student2"]["marks"][-1])


# ============================================================
# 15. LIST vs TUPLE vs SET vs DICTIONARY
# ============================================================

list_example = [1, 2, 2, 3]

tuple_example = (1, 2, 2, 3)

set_example = {1, 2, 3}

dictionary_example = {
    "name": "Devanshu",
    "age": 22
}

print(list_example)
print(tuple_example)
print(set_example)
print(dictionary_example)


# ============================================================
# 16. FUNCTION — POSITIONAL ARGUMENTS
# ============================================================

def greet(name, age):
    print(name, age)


greet("Devanshu", 22)


# ============================================================
# 17. FUNCTION — KEYWORD ARGUMENTS
# ============================================================

greet(age=22, name="Devanshu")


# ============================================================
# 18. DEFAULT ARGUMENTS
# ============================================================

def welcome(name, country="India"):
    print(name, country)


welcome("Devanshu")
welcome("Devanshu", "USA")


# ============================================================
# 19. *args
# ============================================================

def add_all(*args):

    total = 0

    for number in args:
        total += number

    return total


print(add_all(1, 2, 3))
print(add_all(10, 20, 30, 40))
print(add_all())


# ============================================================
# 20. **kwargs
# ============================================================

def show_student(**kwargs):

    print(kwargs)


show_student(
    name="Devanshu",
    age=22,
    branch="CSE"
)

show_student(city="Pune")

show_student()


# ============================================================
# 21. SCOPE
# ============================================================

x = 10


def scope_test():

    x = 20

    print(x)


scope_test()

print(x)


# ============================================================
# 22. LAMBDA
# ============================================================

square = lambda x: x * x

print(square(5))


add = lambda a, b: a + b

print(add(3, 7))


# ============================================================
# 23. LIST COMPREHENSION
# ============================================================

squares = [i * i for i in range(5)]

print(squares)


even_numbers = [
    i for i in range(10)
    if i % 2 == 0
]

print(even_numbers)


# ============================================================
# 24. DICTIONARY COMPREHENSION
# ============================================================

squares_dict = {
    i: i * i
    for i in range(5)
}

print(squares_dict)


even_dict = {
    i: i * i
    for i in range(10)
    if i % 2 == 0
}

print(even_dict)


# ============================================================
# 25. SET COMPREHENSION
# ============================================================

even_set = {
    i * 2
    for i in range(5)
}

print(even_set)


odd_set = {
    i
    for i in range(10)
    if i % 2 == 1
}

print(odd_set)


# ============================================================
# 26. FUNCTION DESIGN — ONE CLEAR RESPONSIBILITY
# ============================================================

def calculate_average(marks):

    total = 0
    count = 0

    for mark in marks:
        total += mark
        count += 1

    return total / count


def calculate_grade(average):

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
grade = calculate_grade(average)

print(f"Average = {average}")
print(f"Grade = {grade}")


# ============================================================
# 27. DRILL — STUDENT MARKS DICTIONARY
# ============================================================

marks = {
    "math": 85,
    "python": 92,
    "physics": 81
}

total = 0
count = 0

for subject, mark in marks.items():

    total += mark
    count += 1

average = total / count

print(f"Total = {total}")
print(f"Average = {average}")


# ============================================================
# 28. DRILL — INVENTORY DICTIONARY
# ============================================================

inventory = {
    "apple": 10,
    "banana": 5,
    "milk": 8
}

inventory["apple"] += 5
inventory["banana"] -= 2
inventory["bread"] = 4

print(inventory)


# ============================================================
# 29. DRILL — WORD FREQUENCY
# ============================================================

sentence = "python is easy python is powerful python"

words = sentence.split()

frequency = {}

for word in words:

    if word in frequency:
        frequency[word] += 1

    else:
        frequency[word] = 1

print(frequency)


# ============================================================
# 30. DRILL — COMMON ELEMENTS USING SETS
# ============================================================

a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

set_a = set(a)
set_b = set(b)

common = set_a & set_b

print(f"Common elements = {common}")


# ============================================================
# 31. DRILL — NESTED DATA TO CLEAN DICTIONARY
# ============================================================

std = [
    ["dev", 75],
    ["rahul", 64],
    ["aman", 52]
]

result = {}

for i in std:

    name = i[0]
    marks = i[1]

    result[name] = marks

print(result)


# ============================================================
# DAY 5 COMPLETE
# ============================================================

print("DAY 5 COMPLETE")