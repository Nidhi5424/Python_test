'''Child (0-12)
Teenager (13-19)
Adult (20-59)
Senior (60+)'''


age = int(input("Enter your age: "))

if age <= 12:
        print("You are a Child.")
else:
    if age <= 19:
        print("You are a Teenager.")
    else:
        if age <= 59:
            print("You are an Adult.")
        else:
            print("You are a Senior.")
if age <=0 :
    print("Invalid age. Age cannot be negative.")

