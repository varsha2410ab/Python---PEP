'''
1. Generate random password
2. Check password strength
3. Count characters
4. Give strength rating
5. Save result in a file
'''

import random
import os

# 1. Define characters (clean & readable)
letters = "abcdefghijklmnopqrstuvwxyz"
LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"

chars = letters + LETTERS + digits

# 2. Generate random password
password = ""

for i in range(8):
    password += random.choice(chars)

print("Password:", password)

# 3. Check password strength
has_upper = False
has_digit = False

for ch in password:
    if ch in LETTERS:
        has_upper = True
    if ch in digits:
        has_digit = True

# 4. Count characters
count = {}
for ch in password:
    if ch in count:
        count[ch] += 1
    else:
        count[ch] = 1

print("Character count:", count)

# 5. Strength rating
if len(password) >= 8 and has_upper and has_digit:
    strength = "Strong"
elif len(password) >= 6:
    strength = "Medium"
else:
    strength = "Weak"

print("Password strength:", strength)

# 6. Save result in a file
if not os.path.exists("result"):
    os.mkdir("result")

file = os.path.join("result", "password.txt")

with open(file, "w") as f:
    f.write("Password: " + password + "\n")
    f.write("Character count: " + str(count) + "\n")
    f.write("Strength: " + strength + "\n")

print("Saved in file:", file)
