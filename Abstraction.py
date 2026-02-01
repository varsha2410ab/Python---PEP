# ABSTRACTION, INTERFACE, COMPOSITION

# Abstraction: Shows only the required data and hides the rest
# -> Defines rules
# -> Shows what to do
# -> Hides how to do
# -> Used in big problems
# -> Mix of Rule class + Ready class

# Abstract Class Example 1
'''class Parent:
    def work(self):
        pass

class Child(Parent):            
    def work(self):
        print("I am working")

c = Child()
c.work()'''

# Abstract Class Example 2
'''class Payment:
    def pay(self, amount):
        pass

class UPI(Payment):
    def pay(self, amount):
        print("Paid using UPI:", amount)

class Card(Payment):
    def pay(self, amount):
        print("Paid using Card:", amount)

class Cash(Payment):
    def pay(self, amount):
        print("Paid using Cash:", amount)

obj = UPI()
obj.pay(2000)

obj = Card()
obj.pay(20000)

obj = Cash()
obj.pay(200)'''

# Abstract Class Example 3
'''class Shape:
    def shape(self):
        pass

class Circle(Shape):
    def shape(self):
        print("This shape is circle")

class Square(Shape):
    def shape(self):
        print("This shape is square")

class Rectangle(Shape):
    def shape(self):
        print("This shape is rectangle")

obj1 = Circle()
obj2 = Square()
obj3 = Rectangle()
obj1.shape()
obj2.shape()
obj3.shape()'''

# Interface Example
'''class Course:
    def course_info(self):        
        print("This is an interesting course")
    def duration(self):            
        pass
    
class ExamInterface:
    def exam_type(self):        
        pass

class PythonCourse(Course, ExamInterface):
    def duration(self):    
        print("Duration is 1 month")
    
    def exam_type(self):    
        print("Exam type is Online")

p = PythonCourse()
p.course_info()
p.duration()
p.exam_type()'''

# Composition Example 1
'''class Address:
    def __init__(self, city):
        self.city = city
    def show_address(self):
        print("City:", self.city)

class Student:
    def __init__(self, name, city):
        self.name = name
        self.address = Address(city)
    def show_student(self):
        print("Name:", self.name)
        self.address.show_address()

s = Student("Varsha", "Delhi")
s.show_student()'''

# Composition Example 2
'''class Engine:
    def start(self):
        print("Engine is started")

class Car:
    def __init__(self):
        self.engine = Engine()

    def drive(self):
        self.engine.start()
        print("Car is moving")

obj = Car()
obj.drive()'''

# Composition Example 3
'''class Subject:
    def __init__(self, name):
        self.name = name
    def show_subject(self):
        print("Subject:", self.name)

class Teacher:
    def __init__(self, name, subject_name):
        self.name = name
        self.subject = Subject(subject_name)
    def show_teacher(self):
        print("Teacher Name:", self.name)
        self.subject.show_subject()

t = Teacher("Varsha", "Math")
t.show_teacher()'''