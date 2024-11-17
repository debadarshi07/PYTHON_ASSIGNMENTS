while True:
    operator = input("Enter the operator(+ , - , * , /) or 'exit' to stop: ")
    if operator == 'exit':
        exit()
    if operator in '+-*/':
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        match operator:
            case '+':
                print(f"{num1} + {num2} = {num1 + num2}")
            case '-':
                print(f"{num1} - {num2} = {num1 - num2}")
            case '*':
                print(f"{num1} * {num2} = {num1 * num2}")
            case '/':
                if num2 != 0:
                    print(f"{num1} / {num2} = {num1 / num2}")
                else:
                    print("Error! Division by zero is not allowed.")
    else:
        print("Invalid operator. Try again.")