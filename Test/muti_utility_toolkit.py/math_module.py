
import math

def math_menu():
    while True:
        print("\n----> Mathematical Operations <----")
        print("1. Calculate Factorial")
        print("2. Solve Compound Interest")
        print("3. Trigonometric Calculations")
        print("4. Area of Geometric Shapes")
        print("5. Back to Main Menu")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            try:
                num = int(input("\nEnter a number: "))
                if num < 0:
                    print("\nFactorial not defined for negative numbers.")
                else:
                    print(f"\nFactorial of {num} is {math.factorial(num)}")
            except ValueError:
                print("\nPlease enter a valid integer.")

        elif choice == "2":
            try:
                p = float(input("\nEnter principal amount: "))
                r = float(input("Enter rate ofinterest ( in %): ")) / 100
                t = float(input("Enter time in years: "))
                n = int(input("Enter compound Interest: "))
                amount = p * (1 + r / n) ** (n * t)
                print(f"\nYour Compound Interest Amount: {round(amount, 2)}")
            except ValueError:
                print("\nInvalid input. Use numbers only.")

        elif choice == "3":
            try:
                angle = float(input("\nEnter angle in degrees: "))
                radians = math.radians(angle)
                print(f"sin({angle}) = {round(math.sin(radians), 4)}")
                print(f"cos({angle}) = {round(math.cos(radians), 4)}")
                print(f"tan({angle}) = {round(math.tan(radians), 4)}")
            except ValueError:
                print("\nInvalid input. Enter a valid number.")

        elif choice == "4":
            print("\nChoose Shape:")
            print("1. Circle")
            print("2. Rectangle")
            print("3. Triangle")

            shape = input("\nEnter choice ): ")

            if shape == "1":
                radius = float(input("\nEnter radius: "))
                area = math.pi * radius ** 2
                print(f"\nArea of Circle: {round(area, 2)}")
            elif shape == "2":
                l = float(input("\nEnter length: "))
                w = float(input("Enter width: "))
                area = l * w
                print(f"\nArea of Rectangle: {round(area, 2)}")
            elif shape == "3":
                b = float(input("\nEnter base: "))
                h = float(input("Enter height: "))
                area = 0.5 * b * h
                print(f"\nArea of Triangle: {round(area, 2)}")
            else:
                print("\nInvalid shape choice.")

        elif choice == "5":
            break

        else:
            print("\nInvalid choice. Please enter 1-5.")
