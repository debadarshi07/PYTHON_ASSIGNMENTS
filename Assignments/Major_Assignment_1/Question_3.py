#Question 3

from Question_2 import tax_amount

def gross_salary(basic_salary):
    allowances = basic_salary * 0.20
    tax = tax_amount(basic_salary)
    gross_salary_per_month = basic_salary + allowances - tax
    return gross_salary_per_month