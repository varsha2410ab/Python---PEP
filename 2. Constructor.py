# CONSTRUCTOR (__init__)

# Constructor is a special method used to initialize objects of a class.
# It runs automatically when an object is created.

# Example 1: Basic constructor with instance variables
'''class Student:
    def __init__(self, name, age):
        self.name = name  # instance variable
        self.age = age

    def show(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Creating objects
s1 = Student("Varsha", 20)
s2 = Student("Rahul", 22)

# Calling method to display data
s1.show()
s2.show()'''


# Example 2: Constructor without parameters
'''class Person:
    def __init__(self):
        self.name = "Unknown"
        self.age = 0

    def show(self):
        print(f"Name: {self.name}, Age: {self.age}")

p1 = Person()
p1.show()'''


# Example 3: Constructor with default parameters
'''class Employee:
    def __init__(self, name="No Name", salary=0):
        self.name = name
        self.salary = salary

    def show(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

e1 = Employee()
e2 = Employee("Ananya", 50000)

e1.show()
e2.show()'''

# SELF Keyword

# 'self' represents the instance of the class.
# It is used to access instance variables and methods within the class.
# It must be the first parameter of instance methods.

# Example 1: Using self to access instance variables
'''class Student:
    def __init__(self, name, age):
        self.name = name  # instance variable
        self.age = age

    def show(self):
        print(f"Name: {self.name}, Age: {self.age}")

s1 = Student("Varsha", 20)
s1.show()'''


# Example 2: Modifying instance variables using self
'''class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def set_age(self, new_age):
        self.age = new_age

    def show(self):
        print(f"Name: {self.name}, Age: {self.age}")

s2 = Student("Rahul", 22)
s2.show()

s2.set_age(23)  # modifying age using method
s2.show()'''


# Example 3: Using self with multiple methods
'''class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, I am {self.name}")

    def rename(self, new_name):
        self.name = new_name

p1 = Person("Varsha")
p1.greet()
p1.rename("Varsha Tiwari")
p1.greet()'''