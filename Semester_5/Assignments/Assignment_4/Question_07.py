def cumulative_sum(list_):
    result_list = []
    sum = 0
    for num in list_:
        sum += num
        result_list.append(sum)
    return result_list

n = int(input("Enter the number of elements: "))
numbers = [int(input("Enter a number: ")) for _ in range(n)]
cumulative_list = cumulative_sum(numbers)
print("Cumulative list:", cumulative_list)