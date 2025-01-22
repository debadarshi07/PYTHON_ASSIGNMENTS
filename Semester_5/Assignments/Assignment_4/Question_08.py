def create_multiples_list(n):
    result = []
    for i in range(1, n + 1):
        result.append([i * j for j in range(1, 6)])
    return result

n = int(input("Enter the value of n: "))
multiples_list = create_multiples_list(n)
print("List of multiples:", multiples_list)