# -------------------------
# EXPENSE TRACKER
# -------------------------
# Flow of the program:
# 1. Start
# 2. Load old expenses from the file
# 3. Show menu:
#    1. Add expense
#    2. View expenses
#    3. Total expense
#    4. Exit
# 4. User selects an option
# 5. Run the corresponding function
# 6. Save data to file
# 7. Repeat until exit
# -------------------------

# File to store expenses
file_name = "Expenses_Tracker.txt"

# Global list to store expenses
# Each expense will be a dictionary: {"Amount": 100, "Category": "Food", "Note": "Lunch"}
expenses = []

# -------------------------
# Load Expenses
# Reads old expenses from file
# -------------------------
def load_data():
    global expenses
    try:
        file = open(file_name, "r")          # Open file in read mode
        lines = file.readlines()              # Read all lines
        file.close()                          # Close file

        # Loop through lines and convert to dictionary
        for line in lines:
            line = line.strip()               # Remove newline
            if line:                          # Skip empty lines
                Amount, Category, Note = line.split(",")  # Split by comma
                expense = {"Amount": int(Amount), "Category": Category, "Note": Note}
                expenses.append(expense)      # Add to global list
    except:
        pass    # If file not found, start with empty expenses

# -------------------------
# Save Expenses
# Writes all expenses to file
# -------------------------
def save_expense():
    global expenses
    file = open(file_name, "w")               # Open file in write mode
    for expense in expenses:                  # Write each expense
        line = f"{expense['Amount']},{expense['Category']},{expense['Note']}\n"
        file.write(line)
    file.close()                              # Close file

# -------------------------
# Add Expense
# Takes input from user and adds to expenses
# -------------------------
def add_expense():
    global expenses
    try:
        amount = int(input("Enter expense amount: "))    # Take amount
        category = input("Enter category: ")            # Take category
        note = input("Enter note: ")                     # Take note
        expense = {"Amount": amount, "Category": category, "Note": note}
        expenses.append(expense)                         # Add to list
        save_expense()                                   # Save updated data
        print("Expense added successfully!")
    except:
        print("Invalid input! Amount must be a number.")

# -------------------------
# View Expenses
# Shows all recorded expenses
# -------------------------
def view_expenses():
    global expenses
    if not expenses:
        print("No expenses recorded yet.")
        return
    print("\n-----All Expenses-----")
    for i, exp in enumerate(expenses, 1):
        print(f"{i}. Amount: {exp['Amount']}, Category: {exp['Category']}, Note: {exp['Note']}")

# -------------------------
# Total Expense
# Calculates sum of all expenses
# -------------------------
def total_expense():
    global expenses
    total = sum(exp["Amount"] for exp in expenses)
    print(f"\nTotal expenses so far: {total}")

# -------------------------
# Main Program
# Controls menu flow
# -------------------------
def main():
    load_data()   # Load previous expenses

    while True:
        print("\n-----EXPENSE TRACKER MENU-----")
        print("1. Add expense")
        print("2. View expenses")
        print("3. Total expense")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expense()
        elif choice == "4":
            print("Thank you for using Expense Tracker!")
            break
        else:
            print("Invalid Choice. Please enter 1-4.")

# Run the program
main()