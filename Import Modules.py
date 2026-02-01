#MATH MODULE
'''import math'''

# math module is used for mathematical operations

# Example 1: Square root
'''num = 16
print(math.sqrt(num))'''

# Example 2: Power of a number
'''print(math.pow(2, 3))'''

# Example 3: Floor value (rounds down)
'''print(math.floor(7.8))'''

# Example 4: Ceil value (rounds up)
'''print(math.ceil(7.8))'''

# Example 5: Absolute value
'''print(math.fabs(-5))'''


#RANDOM MODULE
'''import random'''

# random module is used to generate random numbers or make random selections

# Example 1: Generate random number (dice)
'''dice = random.randint(1, 6)
print(dice)'''

# Example 2: Randomly select a student
'''students = ["Rahul", "Karan", "Vishal", "Neha"]
print(random.choice(students))'''

# Example 3: Generate 4-digit OTP
'''otp = random.randint(1000, 9999)
print(otp)'''


#DATETIME MODULE
'''import datetime'''

#datetime module is sued to work with date and time

# Example 1: Current date and time
'''current = datetime.datetime.now()
print(current)  # current date and time'''

# Example 2: Today's date
'''today = datetime.date.today()
print(today)  # just date'''

# Example 3: Day, month and year separately
'''print(today.day)    # day
print(today.month)  # month
print(today.year)   # year'''

# Example 4: Create specific date
'''date1 = datetime.date(2026, 1, 30)
date2 = datetime.date(2022, 1, 30)
print(date1 - date2)   # difference between dates'''

# Example 5: Add or subtract days using timedelta
'''from datetime import timedelta

future_date = today + timedelta(days=10)  # 10 days later
past_date = today - timedelta(days=5)     # 5 days earlier

print(future_date)
print(past_date)'''


#COLLECTIONS MODULE
'''from collections import Counter'''  

# Counter counts how many times each item appears in a list, tuple, or string

#Example 1: Count items in a list
'''
fruits = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
fruit_count = Counter(fruits)
print(fruit_count)
'''

#Example 2: Count words in a sentence
'''
sentence = "python is easy and python is powerful"
words = sentence.split()       # Split sentence into words
word_count = Counter(words)    # Count frequency of each word
print(word_count)
'''

#Example 3: Count numbers in a list
'''
numbers = [1, 2, 2, 3, 1, 3, 4, 1, 3]
count = Counter(numbers)
print(count)
'''

#OS MODULE
'''import os'''

# os module is used to interact with the operating system
# Examples include getting current directory, listing files, creating folders, checking existence, etc.

#Example 1: Get current working directory
'''
current_path = os.getcwd()   # Returns the current directory
print(current_path)
'''

#Example 2: List files and folders in current directory
'''
files = os.listdir()   # Lists all files and folders
print(files)
'''

#Example 3: Create a folder if it doesn't exist
'''
folder_name = "my_folder"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print("Folder created successfully")
else:
    print("Folder already exists")
'''

#Example 4: Check if a file or folder exists
'''
exists = os.path.exists("imports_examples.py")  # True if file/folder exists
print(exists)
'''

#Example 5: Change current directory
'''
os.chdir("C:/Users")  # Changes the current working directory
print(os.getcwd())    # Verify the new current directory
'''

#SYS MODULE
'''import sys'''
# sys module is used to access system-specific parameters

'''print(sys.version)   # Python version
print(sys.platform)  # Operating system
print(sys.argv)      # Command-line arguments'''