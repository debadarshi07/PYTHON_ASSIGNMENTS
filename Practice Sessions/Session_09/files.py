# File I/O

# Read a file
file = open("testfile.txt", "r")
content = file.read()
print(content)
file.close()

# Write a file
address = "I'm from Bhubaneswar, Odisha, India."
file = open("address.txt", "w")
print(file.write(address))   # by using write() function it overwrites the existing file and returns number of characters written into it.
file.close()

# Read line by line

# readlines()
file = open("multilines.txt", "r")
lines = file.readlines()
print(lines)
file.close()

# readline()
file = open("multilines.txt", "r")
print(file.readline())  # it reads the first line and returns it as a string
print(file.readline())  # it reads the second line and returns it as a string

# using a loop with readline()
line = file.readline()
while line != "":
    print(line.strip())  # strip() is used to remove the newline character
    line = file.readline()
file.close()

# Append to a file
file = open("testfile.txt", "ar")
file.write(address)
file.close()
file = open("testfile.txt", "r")
print(file.read())
file.close()

# with statement - no need to explicitly write the file.close() statement
with open("testfile.txt", "r") as file:
    print(file.read())