# DAY 8 — OOP BASICS
# Date: 28 August 2026


# ============================================================
# 1. CLASS AND OBJECT
# ============================================================

class Student:
    pass


student1 = Student()
student2 = Student()

print(student1)
print(student2)


# ============================================================
# 2. __init__ + INSTANCE ATTRIBUTES
# ============================================================

class Student:

    def __init__(self, name, age, branch):
        self.name = name
        self.age = age
        self.branch = branch


student1 = Student("Devanshu", 22, "CSE")
student2 = Student("Rahul", 21, "CSE")

print(student1.name)
print(student1.age)
print(student1.branch)

print(student2.name)
print(student2.age)
print(student2.branch)


# ============================================================
# 3. METHODS
# ============================================================

class Student:

    def __init__(self, name, age, branch):
        self.name = name
        self.age = age
        self.branch = branch

    def introduce(self):
        return f"My name is {self.name}. I am {self.age} years old."

    def show_branch(self):
        return f"My branch is {self.branch}"


student = Student("Devanshu", 22, "CSE")

print(student.introduce())
print(student.show_branch())


# ============================================================
# 4. CLASS ATTRIBUTES
# ============================================================

class Student:

    college = "ABC Engineering College"

    def __init__(self, name, age):
        self.name = name
        self.age = age


student1 = Student("Devanshu", 22)
student2 = Student("Rahul", 21)

print(student1.college)
print(student2.college)

print(Student.college)


# ============================================================
# 5. INSTANCE ATTRIBUTE VS CLASS ATTRIBUTE
# ============================================================

class Student:

    college = "ABC Engineering College"

    def __init__(self, name):
        self.name = name


student = Student("Devanshu")

print(student.name)
print(student.college)


# ============================================================
# 6. ENCAPSULATION INTUITION
# ============================================================

class BankAccount:

    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance

    def show_balance(self):
        return self._balance


account = BankAccount("Devanshu", 5000)

print(account.owner)
print(account.show_balance())


# ============================================================
# 7. BANK ACCOUNT — DEPOSIT
# ============================================================

class BankAccount:

    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):

        if amount > 0:
            self._balance += amount
            return "Deposit successful."

        return "Amount must be positive."

    def show_balance(self):
        return self._balance


account = BankAccount("Devanshu", 5000)

print(account.deposit(2000))
print(account.show_balance())


# ============================================================
# 8. BANK ACCOUNT — WITHDRAW VALIDATION
# ============================================================

class BankAccount:

    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):

        if amount <= 0:
            return "Amount must be positive."

        self._balance += amount

        return "Deposit successful."

    def withdraw(self, amount):

        if amount <= 0:
            return "Amount must be positive."

        if amount > self._balance:
            return "Insufficient balance."

        self._balance -= amount

        return "Withdrawal successful."

    def show_balance(self):

        return self._balance


account = BankAccount("Devanshu", 5000)

print(account.deposit(1000))
print(account.withdraw(2000))
print(account.withdraw(10000))
print(account.show_balance())


# ============================================================
# 9. INHERITANCE
# ============================================================

class Person:

    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"My name is {self.name}"


class Student(Person):

    def study(self):
        return f"{self.name} is studying."


student = Student("Devanshu")

print(student.introduce())
print(student.study())


# ============================================================
# 10. super()
# ============================================================

class Person:

    def __init__(self, name):
        self.name = name


class Student(Person):

    def __init__(self, name, branch):
        super().__init__(name)
        self.branch = branch


student = Student("Devanshu", "CSE")

print(student.name)
print(student.branch)


# ============================================================
# 11. METHOD OVERRIDING
# ============================================================

class Animal:

    def speak(self):
        return "Animal makes a sound."


class Dog(Animal):

    def speak(self):
        return "Dog barks."


class Cat(Animal):

    def speak(self):
        return "Cat meows."


dog = Dog()
cat = Cat()

print(dog.speak())
print(cat.speak())


# ============================================================
# 12. POLYMORPHISM
# ============================================================

class Dog:

    def speak(self):
        return "Bark"


class Cat:

    def speak(self):
        return "Meow"


class Cow:

    def speak(self):
        return "Moo"


animals = [Dog(), Cat(), Cow()]

for animal in animals:
    print(animal.speak())


# ============================================================
# 13. ABSTRACTION INTUITION
# ============================================================

class Car:

    def start(self):
        self._check_engine()
        print("Car started.")

    def _check_engine(self):
        print("Engine checked.")


car = Car()

car.start()


# ============================================================
# 14. COMPOSITION
# ============================================================

class Engine:

    def start(self):
        return "Engine started."


class Car:

    def __init__(self):
        self.engine = Engine()

    def start(self):
        return self.engine.start()


car = Car()

print(car.start())


# ============================================================
# 15. BASIC DUNDER METHOD — __str__
# ============================================================

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Student(name={self.name}, age={self.age})"


student = Student("Devanshu", 22)

print(student)


# ============================================================
# 16. BASIC DUNDER METHOD — __len__
# ============================================================

class Dataset:

    def __init__(self, data):
        self.data = data

    def __len__(self):
        return len(self.data)


dataset = Dataset([10, 20, 30, 40, 50])

print(len(dataset))


# ============================================================
# 17. DATASET CLASS — LOAD
# ============================================================

class Dataset:

    def __init__(self, data=None):
        self.data = data if data is not None else []

    def load(self, data):
        self.data = data

    def summary(self):
        if not self.data:
            return "Dataset is empty."

        total = 0

        for value in self.data:
            total += value

        mean = total / len(self.data)

        return {
            "count": len(self.data),
            "min": min(self.data),
            "max": max(self.data),
            "mean": mean
        }


dataset = Dataset()

dataset.load([10, 20, 30, 40, 50])

print(dataset.summary())


# ============================================================
# 18. STUDENT CLASS — PRACTICE VERSION
# ============================================================

class Student:

    college = "ABC Engineering College"

    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def average(self):

        total = 0

        for mark in self.marks:
            total += mark

        return total / len(self.marks)

    def grade(self):

        average = self.average()

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

    def introduce(self):

        return (
            f"Name: {self.name}, "
            f"Age: {self.age}, "
            f"Branch: CSE"
        )


student = Student(
    "Devanshu",
    22,
    [85, 92, 78, 90]
)

print(student.introduce())
print(student.average())
print(student.grade())


# ============================================================
# 19. DUNDER METHODS — __repr__ AND __str__
# ============================================================

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"{self.name} - {self.marks}"

    def __repr__(self):
        return f"Student('{self.name}', {self.marks})"


student = Student("Devanshu", 85)

print(str(student))
print(repr(student))


# ============================================================
# 20. FINAL OOP EXAMPLE
# ============================================================

class BankAccount:

    bank_name = "ABC Bank"

    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):

        if amount <= 0:
            return False

        self._balance += amount

        return True

    def withdraw(self, amount):

        if amount <= 0:
            return False

        if amount > self._balance:
            return False

        self._balance -= amount

        return True

    def get_balance(self):

        return self._balance

    def __str__(self):

        return (
            f"BankAccount("
            f"owner={self.owner}, "
            f"balance={self._balance})"
        )


account = BankAccount("Devanshu", 10000)

account.deposit(2000)
account.withdraw(3000)

print(account)
print(account.get_balance())


# ============================================================
# DAY 8 COMPLETE
# ============================================================

print("DAY 8 COMPLETE")