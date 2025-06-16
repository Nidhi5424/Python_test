# multi_utility_toolkit/ (folder)
# │
# |--> main.py                [main control center]
# |--> datetime_module.py     [handles all related to date and time]
# |--> math_module.py         [math oprations]
# |--> random_module.py       [Generates random things]
# |--> uuid_module.py         [Generates a UUID]
# │
# |--> custom_modules/        (Folder for File handling)
#     |--> __init__.py        [this can be empty]
#     |--> file_operations.py [CRWAD oprations]
#     |--> explore.py         [Explore module]
# 



from datetime_module import datetime_menu
from math_module import math_menu
from random_module import random_menu
from uuid_module import generate_uuid
from custom_modules.file_operations import file_menu
from custom_modules.explore import explore_menu

def main():
    while True:
        print("\n===================================")
        print(" Welcome to Multi-Utility Toolkit ")
        print("===================================")
        print("1. Datetime and Time Operations")
        print("2. Mathematical Operations")
        print("3. Random Data Generation")
        print("4. Generate Unique Identifiers (UUID)")
        print("5. File Operations (Custom Module)")
        print("6. Explore Module Attributes (dir())")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            datetime_menu()

        elif choice == "2":
            math_menu()

        elif choice == "3":
            random_menu()

        elif choice == "4":
            generate_uuid()

        elif choice == "5":
            file_menu()

        elif choice == "6":
            explore_menu()

        elif choice == "7":
            print("\nExiting the toolkit...  \n         Goodbye!!!...")
            break

        else:
            print("\nInvalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\nAn error occurred: {e}")
