
num = int(input("Enter a number: "))

if num < 0:
    raise ValueError("Negative number entered! Please enter a positive number.")

print("You entered:", num)
