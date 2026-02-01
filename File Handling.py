# File handling is a way to store data permanently in files and retrieve it whenever needed.

# File Modes:
# 'r'  : Read
# 'w'  : Write (creates or overwrites file)
# 'a'  : Append
# 'r+' : Read + Write

# Writing to a File
print("Example: Writing to a file")
file = open("demo.txt", "w")  # 'w' mode
file.write("Hello Python\n")
file.write("This is file handling\n")
file.close()  # Always close file
print("Data written successfully\n")

# Appending to a File
print("Example: Appending to a file")
file = open("demo.txt", "a")  # 'a' mode
file.write("Appending a new line\n")
file.close()
print("Data appended successfully\n")

# Reading from a File
print("Example: Reading a file")
file = open("demo.txt", "r")  # 'r' mode
content = file.read()
file.close()
print("File Content:\n")
print(content)

# Reading Line by Line
print("Example: Reading line by line")
file = open("demo.txt", "r")
for line in file:
    print(line.strip())  # strip() removes extra newline
file.close()

# Using 'with' Statement (Best Practice)
print("Example: Using 'with' statement")
with open("demo2.txt", "w") as f:
    f.write("Using with statement automatically closes file\n")
print("File written with 'with' statement\n")

# Checking if File Exists (Optional)
import os
if os.path.exists("demo2.txt"):
    print("File exists!")
else:
    print("File does not exist")