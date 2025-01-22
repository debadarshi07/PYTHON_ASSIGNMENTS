def unique_permutations(string_):
    if len(string_) <= 1:
        return {string_}
    
    permutations = set()
    for i in range(len(string_)):
        current_char = string_[i]
        remaining_chars = string_[ : i] + string_[i+1 : ]
        
        for perm in unique_permutations(remaining_chars):
            permutations.add(current_char + perm)

    return permutations

string_ = "abc"
result = unique_permutations(string_)
print(f"All unique permutations of '{string_}':")
for perm in result:
    print(perm)