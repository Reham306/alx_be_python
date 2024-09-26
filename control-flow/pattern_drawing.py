# pattern_drawing.py

# Prompt the user to input the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize a row counter
row = 0

# Use a while loop to go through each row
while row < size:
    # Use a for loop to print asterisks for the current row
    for _ in range(size):
        print("*", end="")  # Print asterisks side by side
    print()  # Move to the next line after printing all asterisks for the current row
    row += 1  # Increment the row counter
