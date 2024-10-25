# import math

# # Calculate the values of e^π and π^e
# e_to_the_pi = math.exp(math.pi)  # e^π
# pi_to_the_e = math.pi ** math.e  # π^e

# # Print the values
# print(f"e^π: {e_to_the_pi}")
# print(f"π^e: {pi_to_the_e}")

# # Compare the values and print the appropriate message
# if e_to_the_pi > pi_to_the_e:
#     print("ok")
# else:
#     print("ok anyway")

# num = int(input("Enter a four digit number: "))
# sum = 0
# numString = ""

# while (num > 0) :
#     digit = num % 10
#     numString += str(digit)
#     sum += digit
#     num //= 10
#     if (num > 0) :
#         numString += " + "

# print(numString," = ", sum)

# Bitwise operator
print(f"2 & 5 : {2 & 5}")
print(f"2 | 5 : {2 | 5}")

# # Output test
# def fun(a = 0 , b = 1):
#     return a ** b + b ** a
# print(f"fun(2, a = 3): {fun(2, a = 3)}") # Error
# print(f"fun(b = 3, a = 2): {fun(b = 3, a = 2)}") # 17
# print(f"fun(): {fun()}") # 1
# print(f"fun(1,2): {fun(1,2)}") # 3

# # Output test
# message = 'Hello Gita'
# print(message[-2:6:-1])
# print(message[8:0])
# print(message[len(message):-1:-1])
# print(message[5:-9:-1])

# print('a' + 3)
# print(4 + 'b')
# print(4 + 3 + 'b')
print("str(5) + 'b':", str(5) + 'b')
# print("int('b')", int('b'))
print("int('10'):", int('10'))
print('ord(b):', ord('b'))