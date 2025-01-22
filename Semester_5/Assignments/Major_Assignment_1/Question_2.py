#Question 2

def tax_amount(basic_salary):
    
    if basic_salary < 60000:
        tax = basic_salary * 0.10
        return tax
    elif 60000 <= basic_salary < 85000:
        tax = basic_salary * 0.15
        return tax
    else:
        tax = basic_salary * 0.20
        return tax