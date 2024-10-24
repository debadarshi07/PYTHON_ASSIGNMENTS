age = int(input('Enter your age: '))
if age > 18:
    print('You are eligible to cast your vote.\n')
elif age < 18 and age > 0:
    print('You are not eligible to cast your vote.\n')
else:
    print('Age can not be negative. Enter valid age.\n')