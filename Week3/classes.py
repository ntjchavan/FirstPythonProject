
class Employee:
    pass

e = Employee()
print(e)
print(type(e))

class Student:
    def study(self):
        print("Student is studying")

stud = Student()
stud.study()

class Employee:
    def work(self):
        print("Employee is working")

    def take_leave(self):
        print("Employee is on leave")

emp = Employee()
emp.work()
emp.take_leave()

class Car:
    def start(self):
        print("Car started")

    def drive(s): # parameter name anything, but it's required else will throw error
        print("Car is Driving")

    def stop(self):
        print("Car Stopped")

car_obj = Car()
car_obj.start()
car_obj.drive()
car_obj.stop()
