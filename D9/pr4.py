
def sum_of_all(num):
    if num < 10:
        return num
    else:
        sum = 0
        while num > 0:
            sum += num % 10    
            num = num // 10          
        return sum_of_all(sum)


n = int(input("Enter a number: "))

print("Single digit sum is:", sum_of_all(n))
