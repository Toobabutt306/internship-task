def calculator():
    # Prompt the user to enter two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Prompt the user to choose an operation
    print("\nChoose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    operation = input("Enter the operation (+, -, *, /): ")

    # Perform the calculation based on the operation chosen
    if operation == '+':
        result = num1 + num2
        print(f"\nThe result of {num1} + {num2} is: {result}")

    elif operation == '-':
        result = num1 - num2
        print(f"\nThe result of {num1} - {num2} is: {result}")

    elif operation == '*':
        result = num1 * num2
        print(f"\nThe result of {num1} * {num2} is: {result}")

    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
            print(f"\nThe result of {num1} / {num2} is: {result}")
        else:
            print("\nError: Division by zero is not allowed.")
    else:
        print("\nInvalid operation. Please choose a valid operation.")

# Call the calculator function
calculator()
