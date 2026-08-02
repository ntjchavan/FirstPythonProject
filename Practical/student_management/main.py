from student import Student
from student_manager import StudentManager

manager = StudentManager()

manager.add_student(Student(101, "Shivam", 16, "FY BSc", "A"))
manager.add_student(Student(102, "Pradnya", 17, "SY BSc", "B"))
manager.add_student(Student(103, "Ajay", 20, "TY BSc", "C"))

manager.view_students()
manager.total_students()

student = manager.search_student(101)
if student:
    print(f"\nStudent found: {student}")
else:
    print("\nStudent not found.")

manager.update_student(102, name="Pradnya Chavan", age=18, student_class="Ty BSc", section="C")
manager.view_students()

manager.delete_student(102)
manager.view_students()
manager.search_by_name("Shivam")
manager.sort_by_name()

# Adding marks for students
manager.add_marks(101, "Maths", 85)
manager.add_marks(101, "Science", 90)
manager.add_marks(101, "Python", 95)
manager.add_marks(101, "Database", 90)
manager.add_marks(103, "Maths",71)
manager.add_marks(103, "Physics", 79)

# Searching for student and viewing marks
print("\nViewing marks for student with ID 103:")
student = manager.search_student(103)
if student:
    print(student)
    student.view_marks()
    print("\nTotal Marks:", student.total_marks())
    print("\nAverage Marks:", f"{student.calculate_average():.2f}")
    subject, marks = student.highest_marks()
    if subject:
        print(f"\nHighest Marks: {marks} in {subject}")

    min_subject, min_marks = student.lowest_marks()
    if min_subject:
        print(f"\nLowest Marks: {min_marks} in {min_subject}")

    print(f"\nHas subject 'Maths': { 'Yes' if student.check_subject('Maths') else 'No' }")
    student.clear_marks()
    print("\n")

else:
    print("Student not found.")

manager.add_marks(101, "Maths", 85)
manager.add_marks(101, "Science", 90)
manager.add_marks(101, "Python", 95)

manager.add_marks(103, "Maths", 77)
manager.add_marks(103, "Science", 78)
manager.add_marks(104, "Python", 85)

manager.show_report_card(101)
manager.show_report_card(103)

# Class level report
print("="*50)
print("Class Report")
print("="*50)
topper = manager.topper()
print(topper.name, f"{topper.percentage:.2f}%")

print(f"Pass Percentage: {manager.pass_percentage():.2f}%")


print("\n")