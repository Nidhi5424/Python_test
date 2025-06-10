#WAP tp print multiplication table of given range.

start = int(input("Enter the starting table number: "))
end = int(input("Enter the ending table number: "))

for i in range(start, end +1):
    print("\nMultiplication Table of",i)
    for j in range(1, 11):
        print(i,"x",j,"=",i*j)
