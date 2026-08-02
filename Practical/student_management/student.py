class Student:
    def __init__(self, student_id, name, age, student_class, section):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.student_class = student_class
        self.section = section

        # Subject => Marks
        self.marks = {}

    def __str__(self):
        return (
            f"Student ID: {self.student_id} | "
            f"Name: {self.name} | "
            f"Age: {self.age} | "
            f"Class: {self.student_class} | "
            f"Section: {self.section}"
        )

    def add_marks(self, subject, marks):
        self.marks[subject] = marks

    def update_marks(self, subject, marks):
        if subject in self.marks:
            self.marks[subject] = marks
            return True

        return False

    def remove_subject(self, subject):
        if subject in self.marks:
            del self.marks[subject]
            return True

        return False

    def view_marks(self):
        if not self.marks:
            print("No marks available.")
            return

        print(f"\nMarks for {self.name}:")
        for subject, marks in self.marks.items():
            print(f"{subject:<15}: {marks}")

    def total_marks(self):
        if not self.marks:
            # print("No marks available.")
            return 0

        return sum(self.marks.values())

    def calculate_average(self):
            if not self.marks:
                # print("No marks available to calculate average.")
                return 0
    
            return sum(self.marks.values()) / len(self.marks)

    def highest_marks(self):
        if not self.marks:
            return None

        for subject, marks in self.marks.items():
            if marks == max(self.marks.values()):
                return subject, marks
            
    def lowest_marks(self):
        if not self.marks:
            return None

        for subject, marks in self.marks.items():
            if marks == min(self.marks.values()):
                return subject, marks

    def check_subject(self, subject):
        if subject in self.marks:
            return True
        
        return False

    def clear_marks(self):
        self.marks.clear()

    @property
    def percentage(self):
        if not self.marks:
            return 0

        return self.total_marks() / len(self.marks)

    @property
    def grade(self):
        percentage = self.percentage

        if percentage >= 90:
            return "A+"
        
        elif percentage >= 80:
            return "A"
        
        elif percentage >= 70:
            return "B"
        
        elif percentage >= 60:
            return "C"
        
        elif percentage >= 50:
            return "D"

        else:
            return "F"

    @property
    def is_passed(self):
        return self.percentage >= 50

    def report_card(self):
        print("="*50)
        print("Student Report Card")
        print("="*50)
        print(f"Student ID : {self.student_id}")
        print(f"Name       : {self.name}")
        print(f"Age        : {self.age}")
        print(f"Class      : {self.student_class}")
        print(f"Section    : {self.section}")

        print("-"*50)
        print("Subject Marks")
        print("-"*50)

        for subject, marks in self.marks.items():
            print(f"{subject:<15} {marks}")

        print("-"*50)
        print(f"Total Marks : {self.total_marks()}")
        print(f"Percentage  : {self.percentage:.2f}%")
        print(f"Grade       : {self.grade}")
        print(f"Result      : { 'Passed' if self.is_passed else 'Failed' }")

        print("="*50)

