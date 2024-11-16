from random import randint as r

def calculate_sum_and_average(random_list):
    total_sum = sum(random_list)
    average = total_sum / len(random_list) if len(random_list) > 0 else 0
    return total_sum, average

random_list = [r(1, 50) for _ in range(5)]
print("Generated random list:", random_list)

total_sum, average = calculate_sum_and_average(random_list)

print(f"Sum of the list: {total_sum}")
print(f"Average of the list: {average:.2f}")