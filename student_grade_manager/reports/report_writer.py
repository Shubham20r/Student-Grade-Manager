def generate_report(students):
    with open("student_report.txt", "w") as f:
        f.write("---- Student Report ----\n")
        for s in students:
            f.write(f"{s.name} | Roll: {s.roll} | Marks: {s.marks} | Grade: {s.grade}\n")
    print("Report generated as 'student_report.txt'.")
