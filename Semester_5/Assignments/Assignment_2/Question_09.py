number = input("Enter a number: ")
isInteger = True
for ch in number:
    if ord(ch) < 48 or ord(ch) > 57 :
        isInteger = False

if isInteger:
    print(f"The remainder dividing number with 5 is: {int(number) % 5}")
else :
    print("Invalid input")