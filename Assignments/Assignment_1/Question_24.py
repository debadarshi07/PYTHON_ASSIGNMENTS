a , b , c = int(input("Enter first number: ")) , int(input("Enter second number: ")) , int(input("Enter third number: ")) 

max_num = max(a, b, c)
min_num = min(a, b, c)
mid_num = (a + b + c) - (max_num + min_num)

print(f"{min_num} < {mid_num} < {max_num}")