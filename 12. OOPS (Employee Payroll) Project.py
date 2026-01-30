# -------------------------
# EMPLOYEE PAYROLL SYSTEM
# -------------------------
# This program calculates salaries for different types of employees
# using Object-Oriented Programming (OOP) concepts in Python.
# Features:
# 1. Full Time Employee
# 2. Part Time Employee
# 3. Encapsulation of salary
# 4. Payroll controller to manage employees
# -------------------------

# -------------------------
# Employee (Abstract Class)
# -------------------------
class Employee:
    def __init__(self, emp_id, name):
        self.emp_id = emp_id       # Employee ID
        self.name = name           # Employee Name

    # Abstract method to calculate salary (to be implemented by child classes)
    def calculate_salary(self):
        pass

# -------------------------
# FullTimeEmployee (Child Class)
# -------------------------
class FullTimeEmployee(Employee):
    def __init__(self, emp_id, name, monthly_salary):
        super().__init__(emp_id, name)
        self._monthly_salary = monthly_salary   # Encapsulated salary

    # Calculate salary for full-time employee
    def calculate_salary(self):
        return self._monthly_salary

# -------------------------
# PartTimeEmployee (Child Class)
# -------------------------
class PartTimeEmployee(Employee):
    def __init__(self, emp_id, name, hours_worked, rate_per_hour):
        super().__init__(emp_id, name)
        self._hours_worked = hours_worked       # Encapsulated hours worked
        self._rate_per_hour = rate_per_hour     # Encapsulated rate

    # Calculate salary for part-time employee
    def calculate_salary(self):
        return self._hours_worked * self._rate_per_hour

# -------------------------
# PayrollApp (Controller / HAS-A)
# -------------------------
class PayrollApp:
    def __init__(self):
        self.employee = None     # Initially no employee

    # Create employee based on type
    def create_employee(self, emp_type):
        if emp_type == "FullTime":
            # Create a full-time employee with example data
            self.employee = FullTimeEmployee(1, "Amit", 50000)
        else:
            # Create a part-time employee with example data
            self.employee = PartTimeEmployee(2, "Neha", 80, 500)
        return "-> Employee Created"

    # Get salary of current employee
    def get_salary(self):
        return self.employee.calculate_salary()

# -------------------------
# Example Usage
# -------------------------
# Full-time employee
app = PayrollApp()
print(app.create_employee("FullTime"))
print("Salary:", app.get_salary())  # Output: 50000

# Part-time employee
app2 = PayrollApp()
print(app2.create_employee("PartTime"))
print("Salary:", app2.get_salary())  # Output: 40000