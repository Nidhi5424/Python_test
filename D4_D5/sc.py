
operator = input("Enter operator (+, -, *, /): ")


num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))


if operator == '+':
    result = num1 + num2
    print("Result:", result)

elif operator == '-':
    result = num1 - num2
    print("Result:", result)

elif operator == '*':
    result = num1 * num2
    print("Result:", result)

elif operator == '/':
    if num2 == 0:
        print("Cannot divide by zero")
    else:
        result = num1 / num2
        print("Result:", result)

else:
    print("Invalid operator")
