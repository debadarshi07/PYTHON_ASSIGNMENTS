print()
# non parametrized function
def wish():
    print("Good Morning")

# parametrized functions
def sum(num1, num2):
    return num1 + num2

def factorial(num):
    result = 1
    if num == 0 or num == 1:
        return result
    for i in range(1, num + 1):
        result *= i
    return result

# default parameters 
# parameters with default arguments must follow parameters without default values.
def wish_someone(name, wish = 'Have a good day !!!'):
    print(f"Hello {name}, {wish}")

def sum1(num, num1 = 2, num2 = 5):
    return num + num1 + num2

# infinite no. of arguments
def print_elements(*args):
    print('Elements are:', end = ' ')
    for arg in args:
        print(arg, end = '   ')

# keyword arguments
def print_key_value_pairs(**kwargs):
    print('Key Value pairs are:')
    for key, value in kwargs.items():
        print(f'{key} = {value}')



# calling all the above functions below

# wish()

# x, y = int(input("Enter first number: ")), int(input("Enter second number: "))
# print(f"Sum of {x} and {y} is {sum(x, y)}.")

# num = int(input("Enter number: "))
# print(f"Factorial of {num} is {factorial(num)}.")

# wish_someone('Debadarshi', 'Good Night !!!')
# wish_someone('Debadarshi')

# print(f"Sum of three numbers: {sum1(10, num2 = 4)}")  # to skip the middle argument and to directly write the next one we need to specify the keyword of corresponding argument.

# print_elements('Debadarshi', 7, 'student', 8.5, [1,2,3], 'ITER', (2,'a',5), {'set',1,10})
# print()
# print_elements([1,2,3,4,5], {'ab',8,7,5,00})

print_key_value_pairs(name = 'Deb', age = 21, college = 'ITER')