num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

minimum = num1

if(minimum > num2):
    minimum = num2

elif(minimum > num3):
    minimum = num3

print("The minimum among three numbers is: ", minimum)