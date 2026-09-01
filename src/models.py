class Student:
    PASS_MARKS = 40
    PASS_ATTENDANCE = 75

    def __init__(self, student_id, name, marks, attendance):
        self.student_id = student_id
        self.name = name
        self.marks = marks
        self.attendance = attendance

    def average(self):
        if not self.marks:
            return 0

        return sum(self.marks) / len(self.marks)

    def is_pass(self):
        return (
            self.average() >= self.PASS_MARKS
            and self.attendance >= self.PASS_ATTENDANCE
        )

    def __str__(self):
        return (
            f"{self.student_id} | "
            f"{self.name} | "
            f"Average: {self.average():.2f} | "
            f"Attendance: {self.attendance}% | "
            f"{'PASS' if self.is_pass() else 'FAIL'}"
        )