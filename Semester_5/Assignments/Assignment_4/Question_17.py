from math import sqrt as sqrt

def compute_standard_deviation(numbers):
    n = len(numbers)
    mean = sum(numbers) / n
    print(f"The mean is {mean:.2f}")
    deviation = sqrt(sum((x - mean) ** 2 for x in numbers) / n)

    return deviation

numbers = [float(input("Enter an integer: ")) for _ in range(10)]
deviation = compute_standard_deviation(numbers)
print(f"Standard Deviation: {deviation:.5f}")