
        

        # student = self.search_student(student_id)
        # if not student:
        #     print(f"Student with ID {student_id} not found.")
        #     return False

        # for key, value in kwargs.items():
        #     if hasattr(student, key):
        #         setattr(student, key, value)
        #         print(f"{key} updated to {value}.")
        #     else:
        #         print(f"{key} is not a valid attribute of Student.")

        # return True

you can replace function with below code as well
def update_student(
        self,
        student_id,
        name=None,
        age=None,
        student_class=None,
        section=None
    ):

        student = self.search_student(student_id)

        if not student:
            return False

        if name:
            student.name = name

        if age:
            student.age = age

        if student_class:
            student.student_class = student_class

        if section:
            student.section = section

        return True
        