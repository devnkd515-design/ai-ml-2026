def calculate_class_average(students):
    if not students:
        return 0

    total = 0

    for student in students:
        total += student.average()

    return total / len(students)


def highest_performer(students):
    if not students:
        return None

    highest = students[0]

    for student in students:
        if student.average() > highest.average():
            highest = student

    return highest


def lowest_performer(students):
    if not students:
        return None

    lowest = students[0]

    for student in students:
        if student.average() < lowest.average():
            lowest = student

    return lowest


def calculate_attendance_average(students):
    if not students:
        return 0

    total = 0

    for student in students:
        total += student.attendance

    return total / len(students)


def search_student(students, query):
    query = str(query).lower()

    results = []

    for student in students:
        if (
            query in student.name.lower()
            or query == str(student.student_id)
        ):
            results.append(student)

    return results


def pass_fail_statistics(students):
    passed = 0
    failed = 0

    for student in students:
        if student.is_pass():
            passed += 1
        else:
            failed += 1

    return {
        "passed": passed,
        "failed": failed
    }