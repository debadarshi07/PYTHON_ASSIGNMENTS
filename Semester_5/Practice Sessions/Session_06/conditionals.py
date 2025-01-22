age = int(input('Enter your age: '))
if age > 18:
    print('You are eligible to cast your vote.\n')
elif age < 18 and age > 0:
    print('You are not eligible to cast your vote.\n')
else:
    print('Age can not be negative. Enter valid age.\n')

day = input('Enter the day of the week: ')
match day:
    case 'Monday':
        print('Today is Monday.')
    case 'Tuesday':
        print('Today is Tuesday.')
    case 'Wednesday':
        print('Today is Wednesday.')
    case 'Thursday':
        print('Today is Thursday.')
    case 'Friday':
        print('Today is Friday.')
    case 'Saturday':
        print('Today is Saturday.')
    case 'Sunday':
        print('Today is Sunday.')
    case _:
        print('Invalid day entered.')