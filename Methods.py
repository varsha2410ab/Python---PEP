# Normal Method

'''class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"Name: {self.name}, Age: {self.age}")

s1 = Student("Varsha", 20)
s1.show()'''


# Class Method

'''class Student:
    school_name = "ABC School"

    @classmethod
    def show_school(cls):
        print(f"School Name: {cls.school_name}")

Student.show_school()'''


# Static Method

'''class Math:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b

print(Math.add(10, 20))
print(Math.multiply(5, 6))'''