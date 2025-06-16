
def file_menu():
    while True:
        print("\n----> File Operations <----")
        print("1. Create a new file")
        print("2. Write to a file")
        print("3. Read from a file")
        print("4. Append to a file")
        print("5. Back to Main Menu")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            filename = input("\nEnter new file name (with .txt): ")
            try:
                with open(filename, 'x') as file:
                    print(f"\n{filename} created successfully.")
            except FileExistsError:
                print("\nFile already exists.")

        elif choice == "2":
            filename = input("\nEnter file name to write to: ")
            text = input("Enter text to write: ")
            try:
                with open(filename, 'w') as file:
                    file.write(text)
                    print("\nFile written successfully.")
            except Exception as e:
                print("\nError:", e)

        elif choice == "3":
            filename = input("\nEnter file name to read: ")
            try:
                with open(filename, 'r') as file:
                    content = file.read()
                    print("\nFile Content:\n-------------")
                    print(content)
            except FileNotFoundError:
                print("\nFile not found.")

        elif choice == "4":
            filename = input("\nEnter file name to append to: ")
            text = input("\nEnter text to append: ")
            try:
                with open(filename, 'a') as file:
                    file.write("\n" + text)
                    print("\nText appended successfully.")
            except Exception as e:
                print("\nError:", e)

        elif choice == "5":
            break

        else:
            print("\nInvalid choice. Please enter 1-5.")
