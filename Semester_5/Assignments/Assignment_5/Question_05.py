tlds = {'Canada': 'ca', 'United States': 'us', 'Mexico': 'mx'}

# a) Check whether the dictionary contains the key 'Canada'.
print("(a) Contains 'Canada':", 'Canada' in tlds)

# b) Check whether the dictionary contains the key 'France'.
print("(b) Contains 'France':", 'France' in tlds)

# c) Iterate through the key-value pairs and display them in a two-column format.
print("(c) Key-Value pairs in two-column format:")
for country, tld in tlds.items():
    print(f"{country}: {tld}")

# d) Add the key-value pair 'Sweden' and 'sw' (incorrect TLD).
tlds['Sweden'] = 'sw'

# e) Update the value for the key 'Sweden' to 'se' (correct TLD).
tlds['Sweden'] = 'se'

# f) Use dictionary comprehension to reverse the keys and values.
reversed_tlds = {value: key for key, value in tlds.items()}

# Displaying results
print("\n(d) Dictionary after adding Sweden with incorrect TLD and updating to correct TLD:")
print(tlds)

print("\n(f) Dictionary with reversed keys and values:")
print(reversed_tlds)