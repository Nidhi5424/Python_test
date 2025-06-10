def check_even(num):
    
    if not isinstance(num, int):
        raise TypeError("Input must be an integer.")

    if num % 2 != 0:
        raise ValueError("The number is odd. Please enter an even number.")

    print("The number is even:", num)


user_input = input("Enter an integer: ")

try:
    number = int(user_input)    
    check_even(number)          
except ValueError as ve:
    print("ValueError:", ve)
except TypeError as te:
    print("TypeError:", te)
