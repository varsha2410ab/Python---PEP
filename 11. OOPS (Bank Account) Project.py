# -------------------------
# BANK ACCOUNT SIMULATION
# -------------------------
# This program simulates a basic bank account system.
# Features:
# 1. Create savings or current account
# 2. Deposit money
# 3. Withdraw money
# 4. Check balance
# 5. Calculate interest
# -------------------------

# -------------------------
# BankAccount (Parent Class)
# -------------------------
class BankAccount:
    def __init__(self, acc_no, name, balance):
        self.acc_no = acc_no          # Account number
        self.name = name              # Account holder's name
        self._balance = balance       # Protected variable to store balance

    # Deposit money into account
    def deposit(self, amount):
        self._balance += amount
        return self._balance

    # Withdraw money from account
    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            return self._balance
        else:
            return "Insufficient balance"

    # Get current balance
    def get_balance(self):
        return self._balance

    # Calculate interest (to be overridden by child classes)
    def calculate_interest(self):
        pass

# -------------------------
# SavingAccount (Child Class)
# -------------------------
class SavingAccount(BankAccount):
    # Savings account earns 4% interest
    def calculate_interest(self):
        interest = self._balance * 0.04
        return interest

# -------------------------
# CurrentAccount (Child Class)
# -------------------------
class CurrentAccount(BankAccount):
    # Current account earns no interest
    def calculate_interest(self):
        return 0

# -------------------------
# BankApp
# This class acts as an interface to the bank account
# -------------------------
class BankApp:
    def __init__(self):
        self.account = None   # Initially no account

    # Create a new account
    def create_account(self, acc_no, name, balance, acc_type):
        if acc_type == "savings":
            self.account = SavingAccount(acc_no, name, balance)
        else:
            self.account = CurrentAccount(acc_no, name, balance)
        return "Account created successfully"

    # Deposit money using the account object
    def deposit_money(self, amount):
        return self.account.deposit(amount)

    # Withdraw money using the account object
    def withdraw_money(self, amount):
        return self.account.withdraw(amount)

    # Check balance using the account object
    def check_balance(self):
        return self.account.get_balance()

    # Get interest using the account object
    def get_interest(self):
        return self.account.calculate_interest()

# -------------------------
# Example Usage
# -------------------------
app = BankApp()

# Create a savings account
print(app.create_account(101, "Shanaya", 10000, "savings"))

# Deposit money
print("Balance after deposit:", app.deposit_money(2000))

# Withdraw money
print("Balance after withdrawing money:", app.withdraw_money(2000))

# Check current balance
print("Current balance:", app.check_balance())

# Calculate interest
print("Interest earned:", app.get_interest())