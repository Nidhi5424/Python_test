
def print_fibonacci(n):
    a, b = 0, 1  
    
    for i in range(n):
        print(a, end=' ')
        a, b = b, a + b 


num = int(input("Enter how many Fibonacci numbers you want: "))

print(f"Fibonacci series till {num}th place is:")
print_fibonacci(num)
