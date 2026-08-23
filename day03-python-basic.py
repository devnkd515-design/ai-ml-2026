# DAY 3 — CONDITIONS + LOOPS
# Date: 23 August 2026

print("\n========== 1. IF ==========")

age = 22

if age >= 18:
    print("Adult")


print("\n========== 2. IF / ELSE ==========")

age = 17

if age >= 18:
    print("Adult")
else:
    print("Minor")


print("\n========== 3. IF / ELIF / ELSE ==========")

age = 25

if age >= 60:
    print("Senior")
elif age >= 18:
    print("Adult")
elif age >= 13:
    print("Teenager")
else:
    print("Child")


print("\n========== 4. TRUTHY / FALSY ==========")

values = [0, 1, "", "Python", None]

for value in values:
    if value:
        print(value, "→ Truthy")
    else:
        print(value, "→ Falsy")


print("\n========== 5. FOR LOOP ==========")

languages = ["Python", "Git", "AI"]

for language in languages:
    print(language)


print("\n========== 6. RANGE ==========")

for i in range(5):
    print(i)


print("\n========== 7. RANGE PATTERNS ==========")

print("2 to 6:")
for i in range(2, 7):
    print(i)

print("Even numbers:")
for i in range(2, 21, 2):
    print(i)

print("Odd numbers:")
for i in range(1, 20, 2):
    print(i)

print("Reverse:")
for i in range(10, 0, -1):
    print(i)


print("\n========== 8. WHILE LOOP ==========")

counter = 1

while counter <= 5:
    print(counter)
    counter += 1


print("\n========== 9. BREAK ==========")

for i in range(10):
    print(i)

    if i == 5:
        break


print("\n========== 10. CONTINUE ==========")

for i in range(10):

    if i == 5:
        continue

    print(i)


print("\n========== 11. PASS ==========")

for i in range(1, 6):

    if i == 3:
        pass

    print(i)


print("\n========== 12. NESTED LOOPS ==========")

for i in range(4):
    for j in range(4):
        print(f"{i}, {j}")


print("\n========== 13. FACTORIAL ==========")

n = 5
fact = 1

for i in range(1, n + 1):
    fact = fact * i

print(f"Factorial of {n} = {fact}")


print("\n========== 14. HCF ==========")

a = 18
b = 28

if a <= b:
    n = a
else:
    n = b

hcf = 1

for i in range(1, n + 1):
    if a % i == 0:
        if b % i == 0:
            hcf = i

print(f"HCF of {a} and {b} = {hcf}")


print("\n========== 15. LCM ==========")

a = 108
b = 116

if a >= b:
    n = a
else:
    n = b

while n % a != 0 or n % b != 0:
    n += 1

print(f"LCM of {a} and {b} = {n}")


print("\n========== 16. FIBONACCI ==========")

# Practice this properly tomorrow.

n = 10

first = 0
second = 1

for i in range(n):
    print(first)

    next_number = first + second
    first = second
    second = next_number


print("\n========== DAY 3 PYTHON COMPLETE ==========")