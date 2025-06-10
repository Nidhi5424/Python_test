# Area and Perimeter 

# circle
radius = float(input("Enter radius of the circle: "))

pi = 3.14
area = pi * radius * radius
perimeter = 2 * pi * radius

print("Area of Circle:", area)
print("Perimeter (Circumference) of Circle:", perimeter)


#squar
side = float(input("Enter side of the square: "))

area = side * side
perimeter = 4 * side

print("Area of Square:", area)
print("Perimeter of Square:", perimeter)


#tringle
a = float(input("Enter side A of triangle: "))
b = float(input("Enter side B of triangle: "))
c = float(input("Enter side C of triangle: "))

s = (a + b + c) / 2
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
perimeter = a + b + c

print("Area of Triangle:", area)
print("Perimeter of Triangle:", perimeter)

#rectengle
length = float(input("Enter length of the rectangle: "))
width = float(input("Enter width of the rectangle: "))

area = length * width
perimeter = 2 * (length + width)

print("Area of Rectangle:", area)
print("Perimeter of Rectangle:", perimeter)
