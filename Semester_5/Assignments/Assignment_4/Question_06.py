numbers = []
for i in range(10):
    num = int(input(f"Enter integer {i + 1}: "))
    numbers.append(num)

element = int(input("Enter the number to search: "))

if element in numbers:
    count = numbers.count(element)
    print(f"The number {element} appears {count} times in the list.")
else:
    print(f"The number {element} is not present in the list.")