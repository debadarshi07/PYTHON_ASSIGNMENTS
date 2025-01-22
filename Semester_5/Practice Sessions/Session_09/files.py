# File I/O

# Read a file
print("Reading a file:\n")

file = open("testfile.txt", "r")
content = file.read()
print(content)
file.close()

# Write a file
print("\nWriting a file:\n")

address = "I'm from Bhubaneswar, Odisha, India."
file = open("address.txt", "w")
print(file.write(address))   # by using the write() function it overwrites the existing file and returns the number of characters written into it.
file.close()

# Read line by line
print("\nReading a file line by line:\n")

# readlines()  - returns the data in a list
print("Using readlines():\n")

file = open("multilines.txt", "r")
lines = file.readlines()
print(lines)
file.close()

# readline()  - returns different lines as strings
print("\nUsing readline():\n")

file = open("multilines.txt", "r")
print(file.readline())  # it reads the first line and returns it as a string
print(file.readline())  # it reads the second line and returns it as a string

# using a loop with readline()
print("\nUsing a loop with readline():\n")

line = file.readline()
while line != "":
    print(line.strip())  # strip() is used to remove the newline character
    line = file.readline()
file.close()

# Append to a file
print("\nAppending to a file:\n")

file = open("testfile.txt", "a")
file.write(address)
file.close()
file = open("testfile.txt", "r")
print(file.read())
file.close()

# with statement - no need to explicitly write the file.close() statement
print("\nUsing with statement:\n")

with open("testfile.txt", "r") as file:
    print(file.read())