import sys

# try and except blocks
try:
    # print(x)
    print(5 / 0)
except NameError:
    print(f"Error Type: {sys.exc_info()[0]}\nError: {sys.exc_info()[1]}")
except:
    print(f"Error Type: {sys.exc_info()[0]}\nError: {sys.exc_info()[1]}")

print()

try:
    print("Hello")
except:
    print("Something went wrong.", sys.exc_info()[1])
else:
    print("Nothing went wrong.")

print()

try:
    x = int(input("Enter a number: "))
    print(x)
except ValueError:
    print("Error: ", sys.exc_info()[1])
finally:
    print("User has entered something.")

print()

try:
    file = open("file1.txt")
    try:
        file.write("Debadarshi Omkar")
    except:
        print("Error: ", sys.exc_info()[1])
    finally:
        file.close()
except:
    print("Error: ", sys.exc_info()[1])

print()

# raise keyword for user defined exception
# a = int(input("Enter a number: "))
# if a < 0:
#     raise Exception("The number can't be negative.")

print()

b = None
try:
    b = int(input("Enter a number: "))
except:
    if not type(b) is int:
        raise TypeError("Only integers are allowed.")