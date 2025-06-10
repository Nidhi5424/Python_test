
for num in range(1, 51):
    if num % 2 == 0:
        if num % 3 == 0:
            print(num,"is divisible by both 2 and 3")
        else:
            print(num," is divisible by 2")
    elif num % 3 == 0:
        print(num,"is divisible by 3")
    else:
        print(num,"is not divisible by 2 or 3")
