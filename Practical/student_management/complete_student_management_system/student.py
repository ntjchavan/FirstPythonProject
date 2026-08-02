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

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "student_class": self.student_class,
            "section": self.section,
            "marks": self.marks
        }
    