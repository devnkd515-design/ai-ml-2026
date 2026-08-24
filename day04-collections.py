# DAY 4 — STRINGS + LISTS
# Date: 24 August 2026


# =========================
# 1. STRING INDEXING
# =========================

text = "Python"

print(text[0])
print(text[2])
print(text[-1])
print(text[-3])


# =========================
# 2. STRING SLICING
# =========================

print(text[0:3])
print(text[2:5])
print(text[:4])
print(text[2:])
print(text[:])
print(text[::2])
print(text[::-1])


# =========================
# 3. STRING METHODS
# =========================

text = "  Hello Python World  "

print(text.upper())
print(text.lower())
print(text.title())
print(text.strip())
print(text.replace("Python", "AI"))
print(text.find("Python"))
print(text.count("o"))
print(text.split())


# =========================
# 4. JOIN
# =========================

words = ["Hello", "Python", "World"]

sentence = " ".join(words)

print(sentence)


# =========================
# 5. LIST CREATION
# =========================

numbers = [10, 20, 30, 40, 50]

print(numbers)
print(numbers[0])
print(numbers[-1])
print(numbers[1:4])
print(numbers[::-1])


# =========================
# 6. LIST MUTATION
# =========================

numbers = [10, 20, 30]

numbers.append(40)
print(numbers)

numbers.extend([50, 60])
print(numbers)

numbers.insert(1, 99)
print(numbers)

numbers.remove(99)
print(numbers)

removed = numbers.pop(1)
print(removed)
print(numbers)


# =========================
# 7. SORT VS SORTED
# =========================

numbers = [5, 2, 8, 1]

numbers.sort()

print(numbers)


numbers = [5, 2, 8, 1]

sorted_numbers = sorted(numbers)

print(numbers)
print(sorted_numbers)


# =========================
# 8. COPYING VS ALIASING
# =========================

a = [10, 20, 30]

b = a

b.append(40)

print(a)
print(b)


# =========================
# 9. ACTUAL COPY
# =========================

a = [10, 20, 30]

b = a.copy()

b.append(40)

print(a)
print(b)


# =========================
# 10. MUTABILITY
# =========================

numbers = [10, 20, 30]

numbers[0] = 99

print(numbers)


# Strings are immutable.
# Example:
#
# text = "Python"
# text[0] = "J"
#
# This causes TypeError.


# =========================
# 11. INDEX ERROR
# =========================

numbers = [10, 20, 30]

print(numbers[0])
print(numbers[1])
print(numbers[2])

# numbers[3] would cause IndexError.


# =========================
# 12. REVERSE STRING
# Without reverse helper
# =========================

text = "hello"

new_string = ""

for i in range(len(text) - 1, -1, -1):
    new_string = new_string + text[i]

print(new_string)


# =========================
# 13. SECOND LARGEST
# =========================

numbers = [10, 25, 8, 40, 32]

largest = numbers[0]
second_largest = numbers[1]

if second_largest > largest:
    largest, second_largest = second_largest, largest

for i in numbers[2:]:

    if i > largest:
        second_largest = largest
        largest = i

    elif i > second_largest:
        second_largest = i

print(f"Largest = {largest}")
print(f"Second largest = {second_largest}")


# =========================
# 14. REMOVE DUPLICATES
# Preserve order
# =========================

numbers = [3, 5, 3, 2, 5, 8, 2]

unique = []

for i in numbers:

    if i not in unique:
        unique.append(i)

print(unique)


# =========================
# 15. WORD FREQUENCY
# =========================

sentence = "python is easy python is fun"

words = sentence.split()

frequency = {}

for word in words:

    if word in frequency:
        frequency[word] = frequency[word] + 1

    else:
        frequency[word] = 1

print(frequency)


# =========================
# 16. COUNT VOWELS
# =========================

text = "hello"

count = 0

vowels = [
    "a", "e", "i", "o", "u",
    "A", "E", "I", "O", "U"
]

for current in text:

    if current in vowels:
        count += 1

print(f"Vowels = {count}")


# =========================
# 17. MENU-DRIVEN LIST MANAGER
# =========================

items = []

while True:

    print("\n1. Add item")
    print("2. Remove item")
    print("3. Show list")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        item = input("Enter item: ")
        items.append(item)

        print("Item added")

    elif choice == "2":

        item = input("Enter item to remove: ")

        if item in items:
            items.remove(item)
            print("Item removed")

        else:
            print("Item not found")

    elif choice == "3":

        print(items)

    elif choice == "4":

        break

    else:

        print("Invalid choice")


print("DAY 4 COMPLETE")