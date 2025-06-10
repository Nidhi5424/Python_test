
arr = [[2,6,2],[5,2,7],[8,4,3]]

sum =0

for i, row in enumerate (arr):
    for j, col in enumerate (row):
        print(arr[i][j], end=" ") 
    sum += col
    print()

print(f"\nSum of all: {sum}")