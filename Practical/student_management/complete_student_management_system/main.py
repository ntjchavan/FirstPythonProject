
from student import Student
from student_manager import StudentManger

manager = StudentManger()
manager.load_students()

while True:
    print("="*80)
    print("Student Management System with JSON file")
    print("="*80)
    print("\n")
    print("1. View Students")
    print("2. Add Students")
    print("3. Save Students")
    print("4. Export to CSV")
    print("5. Sort by Name")
    print("9. Exit")

    choice = int(input("\nEnter you choice: "))

    if choice == 1:
        manager.view_students()

    elif choice == 2:
        id = int(input("ID: "))
        name = input("Name: ")
        age = int(input("Age: "))
        student_class = input("Class: ")
        section = input("section: ")

        subject = input("Subject: ")
        mark = float(input("Mark: "))

        student = Student(id, name, age, student_class, section)
        student.marks = {subject: mark}
        manager.add_student(student)

    elif choice == 3:
        manager.save_data()

    elif choice == 4:
        manager.export_to_csv()

    elif choice == 5:
        manager.sort_by_name()

    elif choice == 9:
        print("Good bye! Thank you!")
        break

    else:
        print("Invalid choice, enter correct choice")

print("\n")