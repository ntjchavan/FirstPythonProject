from student import Student

class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        if self.search_student(student.student_id):
            print(f"Student with ID {student.student_id} already exists.")
            return False

        self.students.append(student)
        print("Student added successfully.")
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

        print("\nList of Students")
        print("-"*80)
        for student in self.students:
            print(student)

    def total_students(self):
        print(f"\nTotal number of students: {len(self.students)}")

    def update_student(self, student_id, **kwargs):
        student = self.search_student(student_id)
        if not student:
            print(f"Student with ID {student_id} not found.")
            return False

        for key, value in kwargs.items():
            if hasattr(student, key):
                setattr(student, key, value)
                print(f"{key} updated to {value}.")
            else:
                print(f"{key} is not a valid attribute of Student.")

        return True

    def delete_student(self, student_id):
        student = self.search_student(student_id)
        if not student:
            print(f"\nStudent with ID {student_id} not found.")
            return False

        self.students.remove(student)
        print(f"\nStudent with ID {student_id} deleted successfully.")
        return True

    def search_by_name(self, name):
        students = [student for student in self.students if student.name.lower() == name.lower()]

        if not students:
            print(f"\nNo students found with name '{name}'.")
            return False

        print(f"\nStudents with name '{name}':")
        for student in students:
            print(student)
        return True

    def sort_by_name(self):
        if not self.students:
            print("No students found.")
            return

        print("\nStudents sorted by name:")
        self.students.sort(key=lambda student: student.name)
        self.view_students()

    def add_marks(self, student_id, subject, marks):
        student = self.search_student(student_id)
        if not student:
            print(f"\nStudent with ID {student_id} not found.")
            return False
        
        student.add_marks(subject, marks)
        return True

    def show_report_card(self, student_id):
        student = self.search_student(student_id)
        if not student:
            print(f"\nStudent with ID {student_id} not found.")
            return False

        student.report_card()
        