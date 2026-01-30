# -------------------------
# ATM SIMULATOR
# -------------------------
# This program simulates an ATM machine.
# Features:
# 1. Check balance
# 2. Deposit money
# 3. Withdraw money
# 4. Change PIN
# 5. Exit
# Data (PIN and balance) is saved in a file: ATM_data.txt
# -------------------------

# File to store ATM data
file_name = "ATM_data.txt"

# Global variables
balance = 1000  # Default account balance
pin = "1234"    # Default ATM PIN

# -------------------------
# Load Data
# Loads saved PIN and balance from the file
# If file doesn't exist, default values are used
# -------------------------
def load_data():
    global balance, pin
    try:
        file = open(file_name, "r")  # Open file in read mode
        lines = file.readlines()      # Read all lines
        file.close()                  # Close file
        pin = lines[0].strip()       # First line is PIN, remove newline
        balance = int(lines[1].strip())  # Second line is balance
    except:
        # If file not found or error occurs, use default balance and PIN
        pass

# -------------------------
# Save Data
# Saves current PIN and balance to the file
# -------------------------
def save_data():
    file = open(file_name, "w")  # Open file in write mode
    file.write(pin + "\n")       # Write PIN
    file.write(str(balance))     # Write balance
    file.close()                 # Close file

# -------------------------
# Check Balance
# Shows current account balance
# -------------------------
def check_balance():
    print("Your balance is:", balance)

# -------------------------
# Deposit Money
# Adds money to the account
# -------------------------
def deposit_money():
    global balance
    try:
        amount = int(input("Enter amount to deposit:"))  # Take input from user
        balance = balance + amount                       # Add to balance
        save_data()                                      # Save updated data
        print("Money deposited successfully")
    except:
        print("Please enter numbers only")             # Handle invalid input

# -------------------------
# Withdraw Money
# Removes money from the account
# -------------------------
def withdraw_money():
    global balance
    try:
        amount = int(input("Enter the amount you want to withdraw:"))  # Take input
        if amount > balance:        # Check if enough balance exists
            print("Insufficient balance!")
        else:
            balance = balance - amount
            save_data()             # Save updated balance
            print("Please collect your cash!")
    except:
        print("Please enter numbers only")  # Handle invalid input

# -------------------------
# Change PIN
# Updates ATM PIN after verifying old PIN
# -------------------------
def change_pin():
    global pin
    old_pin = input("Enter the old pin:")  # Ask for old PIN
    if old_pin == pin:                      # Verify old PIN
        new_pin = input("Enter your new pin:")  # Ask for new PIN
        pin = new_pin
        save_data()                         # Save new PIN
        print("Pin changed successfully!")
    else:
        print("Incorrect pin")              # Old PIN didn't match

# -------------------------
# Main Program
# Controls the entire ATM flow
# -------------------------
def main():
    load_data()                              # Load saved data at start
    user_pin = input("Enter pin:")           # Ask for PIN
    if user_pin != pin:                      # Check if PIN is correct
        print("Incorrect pin")
        return                               # Exit if wrong

    while True:                              # Loop until user exits
        print("\n-----ATM MENU-----")
        print("1. Check balance")
        print("2. Deposit money")
        print("3. Withdraw money")
        print("4. Change pin")
        print("5. Exit")

        choice = input("Enter your choice:")  # Take user choice

        if choice == "1":
            check_balance()                  # Show balance
        elif choice == "2":
            deposit_money()                  # Deposit money
        elif choice == "3":
            withdraw_money()                 # Withdraw money
        elif choice == "4":
            change_pin()                     # Change PIN
        elif choice == "5":
            print("Thank you for using ATM")  # Exit
            break
        else:
            print("Invalid Choice")          # Handle wrong input

# Run the ATM program
main()