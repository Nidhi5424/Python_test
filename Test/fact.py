# Ask the user to enter a number
num = int(input("Enter a number to calculate its factorial: "))

# Use a while loop to check if the number is valid (non-negative)
while num < 0:
    print("\nPlease enter a non-negative number.")
    num = int(input("Enter a number to calculate its factorial: "))

# Initialize factorial to 1
factorial = 1

# Use a for loop to calculate factorial
for i in range(1, num):
    factorial *= i

# Print the result
print("\nThe factorial of",num,"is",factorial)