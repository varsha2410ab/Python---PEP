# POLYMORPHISM

# Polymorphism allows methods to have the same name but behave differently.

# Example 1: Method Overriding (Runtime Polymorphism)
'''class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet(self):
        print("Hello from Child")

p1 = Parent()
p1.greet()

c1 = Child()
c1.greet()'''


# Example 2: Method Overloading using default arguments (Python does not support true overloading)
'''class Math:
    def add(self, a, b=0):
        return a + b

m1 = Math()
print(m1.add(10))       # Uses default b=0
print(m1.add(10, 20))   # Both arguments provided'''


# Example 3: Operator Overloading
'''class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Overloading + operator
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def show(self):
        print(f"Point({self.x}, {self.y})")

p1 = Point(2, 3)
p2 = Point(4, 5)
p3 = p1 + p2  # Uses overloaded +
p3.show()'''