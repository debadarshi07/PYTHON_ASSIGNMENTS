#Question 5

from Question_1 import basic_salary
from Question_2 import tax_amount
from Question_3 import gross_salary
from Question_4 import salary_bracket

def employee_report(employees):

    print("\n" + "+" + "-" * 120 + "+")
    print("|" + "Employee Salary Report".center(120, " ") + "|\n" + "+" + "-"*120 + "+")

    print(f"| {'Name':<25} {'Basic Salary(Rs.)':<25} {'Gross Salary(Rs.)':<25} {'Tax Amount(Rs.)':<25} {'Salary Bracket'} |")
    print("+" + "-" * 120 + "+")

    for name, hourly_rate, hours_worked_per_week in employees:
        monthly_basic_salary = basic_salary(hourly_rate, hours_worked_per_week)
        monthly_gross_salary = gross_salary(monthly_basic_salary)
        tax = tax_amount(monthly_basic_salary)
        income_bracket = salary_bracket(monthly_gross_salary)
        print(f"| {name:<26} {monthly_basic_salary:<25.2f} {monthly_gross_salary:<25.2f} {tax:<25.2f} {income_bracket:<13} |")

    print("|" + "_" * 120 + "|", "\n")


employees = []
for i in range(1, 4):
    print(f"\nEnter the details for Employee{i}.")
    emp_name = input(f"Name: ")
    hourly_rate = float(input(f"Hourly rate: "))
    hours_worked_per_week = float(input(f"Hours worked per week: "))
    employees.append((emp_name, hourly_rate, hours_worked_per_week))


employee_report(employees)