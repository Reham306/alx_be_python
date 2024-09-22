#Develop a simple calculator to do basic math.

#Prompt for user input

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the seconed number: "))
operation = input("Choose the operation (+, -, *, /): ")

#Perform the calculation using match case.

match operation:
    case '+':
        result = num1 + num2
        print(f"The result is {result}")
    case '-':
        result = num1 - num2
        print(f"The result is {result}")
    case '*':
        result = num1 * num2
        print(f"The result is {result}")
    case '/':
        if num2 != 0:
            result = num1 / num2
            print(f"The result is {result}")
        else:
            print("Error: Cannot divide by zero.")
    case _:
        print("Invalid operation. Please choose +, -, *, or /.")
