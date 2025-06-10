x = 20
y = 42

print("Before swapping:", x, y)

# Swapping using XOR

x = x ^ y
y = x ^ y
x = x ^ y

'''
x = x + y
y = x - y
x = x - y
'''

print("After swapping:", x, y)
