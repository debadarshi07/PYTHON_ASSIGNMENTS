def reverse_string(string):
    reverse = ""
    for i in range(len(string) - 1, -1, -1):
        reverse += string[i]
    return reverse

string = input("Enter a string: ")
print(f"Reversed string: {reverse_string(string)}")