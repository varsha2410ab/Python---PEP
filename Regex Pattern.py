import re

# 1. Dot (.) → matches any single character
'''text = "cat cot cut"
result = re.findall(r"c.t", text)
print(result)

# 2. Start of string (^) → checks if string starts with pattern
text = "hello world"
print(bool(re.search(r"^hello", text)))
print(bool(re.search(r"^world", text)))

# 3. End of string ($) → checks if string ends with pattern
text = "hello world"
print(bool(re.search(r"hello$", text)))
print(bool(re.search(r"world$", text)))

# 4. Zero or more (*) → matches 'o' zero or more times
text = "helloooo"
result = re.findall(r"lo*", text)
print(result)

# 5. One or more (+) → matches 'o' one or more times
text = "helloooo"
result = re.findall(r"lo+", text)
print(result)

# 6. Zero or one (?) → optional character
text = "color colour"
result = re.findall(r"colou?r", text)
print(result)

# 7. Character set [] → matches any one character from set
text = "apple ball cat"
result = re.findall(r"[abc]", text)
print(result)

# 8. Digits [0-9] → matches digits
text = "My age is 30"
result = re.findall(r"[0-9]", text)
print(result)

# 9. Small letters [a-z] → matches lowercase letters
text = "My name is Varsha"
result = re.findall(r"[a-z]", text)
print(result)

# 10. Capital letters [A-Z] → matches uppercase letters
text = "My name is VARSHA"
result = re.findall(r"[A-Z]", text)
print(result)

# 11. All letters (A-Z and a-z) → matches both uppercase and lowercase letters
text = "My name is VARSHA"
result = re.findall(r"[A-Za-z]", text)
print(result)

# 12. Digits (\d) → matches digits only
text = "Marks: 90"
result = re.findall(r"\d", text)
print(result)

# 13. Non-digits (\D) → matches everything except digits
text = "Marks: 90"
result = re.findall(r"\D", text)
print(result)

# 14. Words (\w) → matches letters, digits, and underscore
text = "Marks: 90"
result = re.findall(r"\w", text)
print(result)

# 15. Not words (\W) → matches special characters (not letters, digits, underscore)
text = "Marks: 90"
result = re.findall(r"\W", text)
print(result)

# 16. Space (\s) → matches whitespace characters
text = "Marks: 90"
result = re.findall(r"\s", text)
print(result)

# 17. No space (\S) → matches non-whitespace characters
text = "Marks: 90"
result = re.findall(r"\S", text)
print(result)

# 18. Repetition count ({}) → matches exactly 10 digits
text = "Phone: 3472832832"
result = re.findall(r"\d{10}", text)
print(result)

# 19. OR operator (|) → matches either 'cat' or 'dog'
text = "I have a cat and a dog"
result = re.findall(r"cat|dog", text)
print(result)

# 20. Grouping (()) → groups pattern and applies repetition
text = "abab ab"
result = re.findall(r"(ab)+", text)
print(result)'''

# Questions on Regex Pattern:

# 1. Write a regex to validate a 10 digit mobile number
'''import re
mobile = "1234506789"
pattern = r"^\d{10}$"
if re.match(pattern, mobile):
    print("Valid mobile number")
else:
    print("Invalid mobile number")'''

# 2. Write a sentence "Contact me at test@gmail.com or admin@yahoo.in" Extract all the email id from the string
'''import re
text = "Contact me at test@gmail.com or admin@yahoo.in"
pattern = r"[\w.-]+@[\w.-]+\.\w+"
emails = re.findall(pattern, text)
print(emails)'''

# 3. Extract all numbers from a string
'''import re
text = "Order123 price45 quantity6"
numbers = re.findall(r"\d+", text)
print(numbers)'''

# 4. Create a strong password
'''import re
password = "Abc@1234"
pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&]).{8,}$"
if re.match(pattern, password):
    print("Strong password")
else:
    print("Weak password")'''

# 5. Validate a pan number
'''import re
def validate_pan(pan):
    pattern = r'^[A-Z]{5}[0-9]{4}[A-Z]$'
    if re.match(pattern, pan):
        return "Valid PAN"
    else:
        return "Invalid PAN"
user_pan = input("Enter your PAN number: ")
print(validate_pan(user_pan))'''

#6. IPV4
'''import re
def validate_ipv4(ip):
    pattern = r"^(\d{1,3}\.){3}\d{1,3}$"
    if re.match(pattern, ip):
        return "Valid IPv4"
    else:
        return "Invalid IPv4"
ip = input("Enter IPv4 address: ")
print(validate_ipv4(ip))'''

#7. IPV6
'''import re
def validate_ipv6(ip):
    pattern = r"^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$"
    if re.match(pattern, ip):
        return "Valid IPv6"
    else:
        return "Invalid IPv6"
ip = input("Enter IPv6 address: ")
print(validate_ipv6(ip))'''

#8. Hexadecimal
'''import re
def validate_hex(hex_value):
    pattern = r'^[0-9a-fA-F]+$'
    if re.match(pattern, hex_value):
        return "Valid Hexadecimal"
    else:
        return "Invalid Hexadecimal"
hex_value = input("Enter hexadecimal value: ")
print(validate_hex(hex_value))'''