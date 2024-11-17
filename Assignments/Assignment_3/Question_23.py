def vowel_indices(input_string):
    indices = []

    for index, char in enumerate(input_string):
        if char in "aeiouAEIOU":
            indices.append(index)

    return indices

input_str = input("Enter a string: ")
print(f"Indices of vowels in '{input_str}' : {vowel_indices(input_str)}.")