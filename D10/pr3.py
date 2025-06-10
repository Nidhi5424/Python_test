arr = []



row=2
col=3

for i in range(row):
    a = []
    for j in range(col):
        a.append(int(input("Enter array elements:")))
    arr.append(a)

for i, row in enumerate (arr):
   for j, col in enumerate (row):
       print(arr[i][j], end=" ") 
   print()


transpose = []
  
for i, col in enumerate (row):
    new_row = [] 
    for j, row in enumerate (arr):
        new_row.append(arr[j][i]) 
    transpose.append(new_row)

print("\nTransposed 3x2 Matrix:")
for row in transpose:
    for val in row:
        print(val, end=" ")
    print()


