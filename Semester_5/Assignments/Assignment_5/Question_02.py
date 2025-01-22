def create_student_dict():
    student_dict = {}
    num_students = int(input("Enter the number of students: "))

    for _ in range(num_students):
        name = input("Enter student name: ")
        percentage = float(input(f"Enter percentage for {name}: "))
        student_dict[name] = percentage

    return student_dict

def display_student_info(student_dict):
    for name, percentage in student_dict.items():
        print(f"Name: {name}, Percentage: {percentage}%")

student_dict = create_student_dict()
display_student_info(student_dict)