
import random
import string

def random_menu():
    while True:
        print("\n----> Random Data Generation <----")
        print("1. Generate a Random Number")
        print("2. Create a Random Password")
        print("3. Generate a Random OTP")
        print("4. Back to Main Menu")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            try:
                low = int(input("\nEnter lower bound: "))
                high = int(input("Enter upper bound: "))
                if low > high:
                    print("\nLower bound must be less than upper bound.")
                else:
                    print(f"\nRandom number: {random.randint(low, high)}")
            except ValueError:
                print("\nPlease enter valid integers.")

        elif choice == "2":
            try:
                length = int(input("\nEnter password length: "))
                characters = string.ascii_letters + string.digits + string.punctuation
                password = ''.join(random.choices(characters, k=length))
                print(f"\nRandom Password: {password}")
            except ValueError:
                print("\nPlease enter a valid length.")

        elif choice == "3":
            otp = ''.join(random.choices(string.digits, k=6))
            print(f"\nYour OTP is: {otp}")

        elif choice == "4":
            break

        else:
            print("\nInvalid choice. Please enter 1-4.")
