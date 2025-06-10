
arr = [
    [12, 45, 74],
    [33, 84, 29],
    [11, 67, 22]
]

max_value = arr[0][0]

for row in arr:
    for element in row:
        if element > max_value:
            max_value = element

print(f"Max value: {max_value}")

min_value = arr[0][0]

for row in arr:
    for element in row:
        if element < min_value:
            min_value = element

print(f"Max value: {min_value}")
