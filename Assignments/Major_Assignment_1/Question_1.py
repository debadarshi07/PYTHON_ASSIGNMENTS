# Question 1

def basic_salary(hourly_rate, hours_worked_per_week):
   basic_salary_per_month = hourly_rate * min(hours_worked_per_week, 40) * 4
   return basic_salary_per_month

def overtime_salary(hourly_rate, hours_worked_per_week):
    extra_hours_worked_per_week = max(0, hours_worked_per_week - 40)
    overtime_salary_per_month = extra_hours_worked_per_week * hourly_rate * 1.5 * 4
    return overtime_salary_per_month

def total_salary(hourly_rate, hours_worked_per_week):
    basic_salary_per_month = basic_salary(hourly_rate, hours_worked_per_week)
    overtime_salary_per_month = overtime_salary(hourly_rate, hours_worked_per_week)
    total_salary_per_month = basic_salary_per_month + overtime_salary_per_month
    return total_salary_per_month