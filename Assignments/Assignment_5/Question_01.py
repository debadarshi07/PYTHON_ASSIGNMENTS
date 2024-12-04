def create_student_dict():
    student_dict = {}
    num_students = int(input("Enter the number of students: "))

    for _ in range(num_students):
        name = input("Enter student name: ")
        marks = float(input(f"Enter marks for {name}: "))
        student_dict[name] = marks

    return student_dict

def display_student_marks(student_dict):
    student_name = input("Enter student name to display marks: ")

    if student_name in student_dict:
        print(f"Marks for {student_name}: {student_dict[student_name]}")
    else:
        print(f"Student {student_name} not found in the record.")

student_dict = create_student_dict()
display_student_marks(student_dict)