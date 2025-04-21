# 🎓 Student Grade Manager (Console App)

This is a simple console-based application developed in **Python** for managing student records, calculating grades, and generating performance reports — all **without using a database**.

## 🚀 Features

- Add student records (Name, Roll Number, Marks)
- Calculate average and assign grades
- Display all students' details
- Generate report as a `.txt` file
- Fully modular code using custom packages and modules

## 📁 Project Structure:
css
Copy
Edit
student_grade_manager/
│
├── main.py
├── grades/
│   ├── __init__.py
│   ├── student.py
│   └── grade_utils.py
└── reports/
    └── report_writer.py

## 🛠️ How to Run

1. Make sure you have Python 3 installed.
2. Clone or download this repository.
3. Open your terminal and navigate to the project folder.
4. Run the application:

```bash
python main.py
📜 Example Usage
pgsql
Copy
Edit
--- Student Grade Manager ---
1. Add Student
2. View All Students
3. Generate Report
4. Exit

Enter your choice: 1
Enter student name: Alice
Enter roll number: 101
Enter marks (space-separated): 89 92 85
Student added successfully.
📄 Sample Output (student_report.txt)
yaml
Copy
Edit
---- Student Report ----
Alice | Roll: 101 | Marks: [89, 92, 85] | Grade: A
👥 Team Members
Student 1 - Team Leader

Student 2 - UI & Logic

Student 3 - Report Module

Student 4 - Grade Logic

Student 5 - Testing & Debugging

🔍 This project was developed as part of a Python learning activity for B.Tech students. No database or external packages were used.

📌 Requirements
Python 3.x

No third-party libraries required
