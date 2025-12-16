# Simple Calculator Program

# Take input from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Select operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choice = input("Enter choice (+, -, *, /): ")

# Perform calculation
if choice == '+':
    result = num1 + num2
    print("Result =", result)

elif choice == '-':
    result = num1 - num2
    print("Result =", result)

elif choice == '*':
    result = num1 * num2
    print("Result =", result)

elif choice == '/':
    if num2 != 0:
        result = num1 / num2
        print("Result =", result)
    else:
        print("Error: Division by zero")

else:
    print("Invalid operation")
