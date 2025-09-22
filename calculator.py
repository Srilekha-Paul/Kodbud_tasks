# Simple CLI Calculator
print("Welcome to the Simple CLI Calculator!")

# Print welcome message
print("Operations available: +, -, *, /")

# Take input from the user
num1 = float(input("Enter the first number: "))
operator = input("Enter an operation (+, -, *, /): ")
num2 = float(input("Enter the second number: "))

# Perform calculation based on operator
if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    # Handle division by zero
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero."
else:
    result = "Invalid operator!"

# Display result
print(f"The result is: {result}")
