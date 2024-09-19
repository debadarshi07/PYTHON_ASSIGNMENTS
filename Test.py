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
