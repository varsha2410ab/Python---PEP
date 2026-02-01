# An exception is an error that occurs while the program is running,
# which stops the normal flow of the program.
# Example: dividing by zero, invalid input, file not found.

# Why Handle Exceptions?
# - To prevent the program from crashing
# - To show meaningful error messages
# - To continue program execution safely

# Basic try-except
print("Example: Basic try-except")
try:
    a = int(input("Enter a number: "))
    print("10 divided by your number is:", 10 / a)
except:
    print("Error occurred")
print()

# Specific Exception Handling
print("Example: Handling specific exceptions")
try:
    b = int(input("Enter a number: "))
    print("10 divided by your number is:", 10 / b)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input, please enter a number")
print()

# try-except-else
print("Example: try-except-else")
try:
    c = int(input("Enter a number: "))
    result = 10 / c
except:
    print("Error occurred")
else:
    print("Result is:", result)
print()

# finally block
print("Example: finally block")
try:
    d = int(input("Enter a number: "))
    print("10 divided by your number is:", 10 / d)
except:
    print("Error occurred")
finally:
    print("This block always executes")
print()

# Combining with File Handling (Optional)
print("Example: Exception handling with file")
try:
    file = open("nonexistent.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("File not found")
finally:
    print("Program executed")