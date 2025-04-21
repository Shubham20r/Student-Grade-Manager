from grades.student import Student
from grades.grade_utils import calculate_grade
from reports.report_writer import generate_report

students = []

def show_menu():
    print("\n--- Student Grade Manager ---")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Generate Report")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter student name: ")
        roll = input("Enter roll number: ")
        marks = list(map(int, input("Enter marks (3 or more space-separated): ").split()))
        student = Student(name, roll, marks)
        student.grade = calculate_grade(student.marks)
        students.append(student)
        print("Student added successfully.")

    elif choice == '2':
        for s in students:
            print(s)

    elif choice == '3':
        generate_report(students)

    elif choice == '4':
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
