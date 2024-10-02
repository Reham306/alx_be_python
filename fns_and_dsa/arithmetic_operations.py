# arithmetic_operations.py

def perform_operation(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:  # Check for division by zero here
            return "Division by zero is not allowed"  # Handle division by zero
        else:
            return num1 / num2  # Perform the division if num2 is not zero
    else:
        return "Invalid operation"  # Handle invalid operations
