from datetime import datetime
import time

def date_difference():
    try:
        date1 = input("\nEnter the first date (YYYY/MM/DD): ")
        date2 = input("Enter the second date (YYYY/MM/DD): ")

        date_obj1 = datetime.strptime(date1, "%Y/%m/%d")
        date_obj2 = datetime.strptime(date2, "%Y/%m/%d")

        diff = abs((date_obj2 - date_obj1).days)
        print(f"\nDifference between dates is {diff} day(s).")
    except ValueError:
        print("\nInvalid date format. Please use YYYY/MM/DD.")

def stopwatch():
    try:
        st = int(input("Enter seconds to run stopwatch: "))
        for i in range(st, 0, -1):
            print(f"⏱️  Stopwatch: 00:00:{i:02d}", end="\r")
            time.sleep(1)
        print("⏱️  Time Up!!!           ")
    except ValueError:
        print("Please enter a valid number.")

def countdown_timer():
    try:
        sec = int(input("Enter countdown time in seconds: "))
        while sec:
            print(f"⏳ Time left: {sec} seconds", end="\r")
            time.sleep(1)
            sec -= 1
        print("⏳ Time's up!             ")
    except ValueError:
        print("Please enter a valid number.")

def datetime_menu():
    while True:
        print("\n----> Datetime and Time Operations <----")
        print("1. Display the current date and time")
        print("2. Calculate the difference between two dates")
        print("3. Format date into custom format")
        print("4. Stopwatch")
        print("5. Countdown Timer")
        print("6. Back to Main Menu")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            now = datetime.now()
            print("\nCurrent Date and Time:", now.strftime("%Y/%m/%d %H:%M:%S"))

        elif choice == "2":
            date_difference()

        elif choice == "3":
            now = datetime.now()
            custom_format = now.strftime("%d/%b/%Y %I:%M %p")
            print("\nFormatted Date & Time:", custom_format)

        elif choice == "4":
            stopwatch()

        elif choice == "5":
            countdown_timer()

        elif choice == "6":
            break

        else:
            print("\nInvalid choice. Please enter a number from 1 to 6.")
