# Simple Calculator Program

print("------ Simple Calculator ------")

# Take input from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("Choose operation: + (Add), - (Subtract), * (Multiply), / (Divide)")
operation = input("Enter operation: ")

# Perform calculation
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero."
else:
    result = "Invalid operation!"

# Display result
print("Result:", result)
