from student import Student
import json
import csv
import logging

logging.basicConfig(
    filename="students.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

class StudentManger:
    def __init__(self):
        self.students = []

    def load_students(self, filename="student.json"):
        try:
            with open(filename, "r") as file:
                data = json.load(file)

            self.students = []
            for item in data:
                student = Student(item["student_id"], item["name"], item["age"], item["student_class"], item["section"])
                student.marks = item["marks"]

                self.students.append(student)

            print("\nStudents loaded!")

        except FileNotFoundError:
            print(f"No saved data found.")

        except json.JSONDecodeError:
            print("Invalid JSON file.")

    def add_student(self, student):
        if self.search_student(student.student_id):
            print(f"Student with ID {student.student_id} already exists.")
            return False

        self.students.append(student)
        print("Student added successfully.")
        logging.info(f"Student Added: {student.student_id}")
        return True

    def search_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student

        return None
    
    def view_students(self):
        if not self.students:
            print("No students found.")
            return

        print("\nList of students:")
        print("-"*80)
        for student in self.students:
            print(student)

    def save_data(self, filename="student.json"):
        data = []

        for student in self.students:
            print(student.to_dict())
            data.append(student.to_dict())

        with open(filename, "w") as file:
            json.dump(data, file, indent=4)

        print("Data saved successfully!")

    def export_to_csv(self, filename="students.csv"):
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)

            writer.writerow([
                "ID",
                "Name",
                "Age",
                "Class",
                "Section"
            ])

            for student in self.students:
                writer.writerow([
                    student.student_id,
                    student.name,
                    student.age,
                    student.student_class,
                    student.section
                ])

            print("CSV Exported!")

    def sort_by_name(self):
        self.students.sort(
            key=lambda student: student.name
        )