
def factorial(n):
    if n < 0:
        return "Invalid! \nFactorial of a negative number doesn't exist."
    elif n == 0 or n == 1:
        return 1  
    else:
        return n * factorial(n - 1)  


num = int(input("Enter a number: "))

print("Factorial is:", factorial(num))



