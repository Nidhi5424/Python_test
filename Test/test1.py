import datetime


print("Welcome to the Interactive Personal Data Collector!\n")

name = input("Please Enter Your Name:")
age = int(input("Please Enter Your Age:"))
height = float(input("Please Enter Your Height in Meters:"))
number = int(input("Please Enter Your Favourite Number:"))

print("\n Thank Ypu! Here is the information we collected:\n")

print("Name:", name,"(Type:",type(name),"," "Memory Address:)", id(name),")")

print("Age:", age, "(Type:",type(age),"," "Memory Address:)", id(age),")")

print("Height:",height,"(Type:",type(height),"," "Memory Address:)", id(height),")")

print("Favourite Number:",number,"(Type:",type(number),"," "Memory Address:)", id(number),")")

current_year = datetime.datetime.now().year
year = current_year - age 
print("\n Your birth year is approximately:",year, "(based on your age of)\n")

print("Thank You for using the Personal Data Collector. Goodbye!")

