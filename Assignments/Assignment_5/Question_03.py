def get_user_input_dict():
    dict_ = {}
    total_entries = int(input("Enter the number of entries in the dictionary: "))

    for _ in range(total_entries):
        key = input("Enter key: ")
        value = float(input(f"Enter value for {key}: "))
        dict_[key] = value

    return dict_

def sum_of_values(dict_):
    return sum(dict_.values())

dict_ = get_user_input_dict()
total_sum = sum_of_values(dict_)
print(f"The sum of the values in the dictionary is: {total_sum}")