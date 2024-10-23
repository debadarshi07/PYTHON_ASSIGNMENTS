print()

student_1 = {
    'name' : 'Debadarshi Omkar',
    'reg_no' : 2241015006,
    'branch' : 'CSE',
    'cgpa' : 9.0,
    'is_passed' : True,
    'sgpa_list' : [9.29, 8.82, 9.29, 9]
}

# dictionary methods
# keys(), values() and items()
print('keys:', student_1.keys(), '\n')
print('values:', student_1.values(), '\n')
print('items:', student_1.items(), '\n')

# update() and get()
student_1.update({'cgpa' : 8.9, 'is_dayscholar' : True})
print('Updated student_1:', student_1, '\n')

print('Name of student_1 is:', student_1.get('name')) # It returns None if key is not present in dictionary
print('Name of student_1 is:', student_1['name'], '\n') # It throws error if key is not present in dictionary

# pop() and popitem()
# popped = student_1.pop('section', 'not found')
# print('Popped value: ', popped)
# popped = student_1.pop('is_dayscholar', 'not found')
# print('Popped value: ', popped, '\n')

# popped_item = student_1.popitem()
# print('Popped item:', popped_item)
# popped_item = student_1.popitem()
# print('Popped item:', popped_item, '\n')

# clear()
# student_1.clear()
# print('student_1 after clear:', student_1, '\n')

print('Final student_1 dictionary is:', student_1, '\n')
print('Final student_1 dictionary is:', student_1.items(), '\n')