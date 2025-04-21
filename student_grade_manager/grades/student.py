class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks
        self.grade = ""

    def __str__(self):
        return f"{self.name} | Roll: {self.roll} | Marks: {self.marks} | Grade: {self.grade}"