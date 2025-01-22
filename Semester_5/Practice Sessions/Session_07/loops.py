print()
list1 = ['student3', 'student2', 'student5', 'student9', 'student6', 'student4', 'student1', 'student7']

# while loop
print('List1 using while loop: ')
index = 0
while index < len(list1):
    print(list1[index], end = ' ')
    index += 1
print('\n')

# for loop
print('List1 using for loop:')
# for i in range(len(list1)):
#     print(list1[i], end = ' ')
for element in list1:
    print(element, end = ' ')
print('\n')