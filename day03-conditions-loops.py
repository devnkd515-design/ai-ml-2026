# DAY 3 — CONDITIONS + LOOPS
# Date: 23 August 2026


# =========================
# 1. IF / ELIF / ELSE
# =========================

age = 22

if age >= 18:
    print("Adult")
else:
    print("Minor")


marks = 85

if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
else:
    print("Grade F")


# =========================
# 2. TRUTHY / FALSY
# =========================

value = 0

if value:
    print("Truthy")
else:
    print("Falsy")


# =========================
# 3. FOR LOOP
# =========================

for i in range(5):
    print(i)


# =========================
# 4. RANGE PATTERNS
# =========================

for i in range(2, 7):
    print(i)

for i in range(2, 21, 2):
    print(i)

for i in range(10, 0, -1):
    print(i)


# =========================
# 5. WHILE LOOP
# =========================

count = 1

while count <= 5:
    print(count)
    count += 1


# =========================
# 6. BREAK
# =========================

for i in range(10):
    print(i)

    if i == 5:
        break


# =========================
# 7. CONTINUE
# =========================

for i in range(10):

    if i == 5:
        continue

    print(i)


# =========================
# 8. PASS
# =========================

for i in range(5):

    if i == 2:
        pass

    print(i)


# =========================
# 9. NESTED LOOPS
# =========================

for i in range(4):

    for j in range(4):
        print(f"{i}, {j}")


# =========================
# 10. FACTORIAL
# =========================

n = 5
fact = 1

for i in range(1, n + 1):
    fact = fact * i

print(f"Factorial = {fact}")


# =========================
# 11. HCF
# =========================

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

print(f"HCF = {hcf}")


# =========================
# 12. LCM
# =========================

a = 108
b = 116

if a >= b:
    n = a
else:
    n = b

while n % a != 0 or n % b != 0:
    n += 1

print(f"LCM = {n}")


# =========================
# 13. FIBONACCI
# =========================

n = 10

fr = 0
sc = 1

for i in range(n):

    print(fr)

    nx = fr + sc
    fr = sc
    sc = nx


# =========================
# 14. PRIME NUMBER
# =========================

n = 13

if n <= 1:

    print("Not Prime")

else:

    prime = True

    for i in range(2, n):

        if n % i == 0:
            prime = False
            break

    if prime:
        print("Prime")
    else:
        print("Not Prime")


# =========================
# 15. PALINDROME
# =========================

text = "madam"

reverse = ""

for i in range(len(text) - 1, -1, -1):
    reverse = reverse + text[i]

if text == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")


# =========================
# 16. EVEN / ODD
# =========================

n = 10

if n % 2 == 0:
    print("Even")
else:
    print("Odd")


# =========================
# 17. LARGEST OF THREE
# =========================

a = 10
b = 25
c = 15

if a >= b and a >= c:
    largest = a

elif b >= a and b >= c:
    largest = b

else:
    largest = c

print(f"Largest = {largest}")


# =========================
# 18. COUNT VOWELS
# =========================

text = "hello"

count = 0
vowels = ["a", "e", "i", "o", "u",
          "A", "E", "I", "O", "U"]

for current in text:

    if current in vowels:
        count += 1

print(f"Vowels = {count}")


# =========================
# 19. MULTIPLICATION TABLE
# =========================

n = 7

for i in range(1, 11):

    result = i * n

    print(f"{n} x {i} = {result}")


print("DAY 3 COMPLETE")