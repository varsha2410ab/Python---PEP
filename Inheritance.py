# INHERITANCE

# Inheritance allows a class (child) to acquire properties and methods of another class (parent).

# Example 1: Single Inheritance
'''class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, I am {self.name}")

class Student(Person):
    def student_id(self, sid):
        print(f"My ID is {sid}")

s1 = Student("Varsha")
s1.greet()
s1.student_id(101)'''


# Example 2: Multiple Inheritance
'''class Teacher:
    def subject(self, sub):
        print(f"I teach {sub}")

class Mentor(Person, Teacher):
    def mentor_id(self, mid):
        print(f"My Mentor ID is {mid}")

m1 = Mentor("Ananya")
m1.greet()
m1.subject("Math")
m1.mentor_id(201)'''


# Example 3: Multilevel Inheritance
'''class GrandParent:
    def family_name(self):
        print("Family Name: Sharma")

class Parent(GrandParent):
    def parent_name(self):
        print("Parent Name: Rahul")

class Child(Parent):
    def child_name(self):
        print("Child Name: Varsha")

c1 = Child()
c1.family_name()
c1.parent_name()
c1.child_name()'''


# Example 4: Hierarchical Inheritance
'''class Animal:
    def species(self):
        print("I am an animal")

class Dog(Animal):
    def dog_name(self):
        print("Dog Name: Bruno")

class Cat(Animal):
    def cat_name(self):
        print("Cat Name: Whiskers")

d1 = Dog()
d1.species()
d1.dog_name()

c1 = Cat()
c1.species()
c1.cat_name()'''