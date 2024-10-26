#Question 4

def salary_bracket(gross_salary):
    if gross_salary < 50000:
        return "Low income"
    elif 50000 < gross_salary < 80000:
        return "Middle income"
    else:
        return "High income"