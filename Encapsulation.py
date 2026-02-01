# ENCPSULATION

# Encapsulation is the process of restricting access to some variables and methods.
# In Python, we use _ (protected) and __ (private) to encapsulate.

# Example 1: Public attributes
'''class Student:
    def __init__(self, name, age):
        self.name = name  # public
        self.age = age    # public

s1 = Student("Varsha", 20)
print(s1.name)
print(s1.age)'''


# Example 2: Protected attributes
'''class Student:
    def __init__(self, name, age):
        self._name = name   # protected
        self._age = age     # protected

s2 = Student("Rahul", 22)
print(s2._name)
print(s2._age)'''


# Example 3: Private attributes with getter and setter
'''class Student:
    def __init__(self, name, age):
        self.__name = name   # private
        self.__age = age     # private

    # Getter methods
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    # Setter methods
    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

s3 = Student("Ananya", 21)

# Accessing private attributes using getters
print(s3.get_name())
print(s3.get_age())

# Modifying private attributes using setters
s3.set_name("Varsha")
s3.set_age(23)

print(s3.get_name())
print(s3.get_age())'''