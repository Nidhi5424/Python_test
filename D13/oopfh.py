class FileHandler:
    def __init__(self, filename):
        self.filename = filename + ".txt"

    def write_file(self, content):
        with open(self.filename, 'w') as file:
            file.write(content)
        print("\nFile written successfully.")

    def append_file(self, content):
        with open(self.filename, 'a') as file:
            file.write(content)
        print("\nFile appended successfully.")

    def read_file(self):
        with open(self.filename, 'r') as file:
            data = file.read()
            print("\n ~~~~~~~~~: File Content ~~~~~~~~~:")
            print(data)



filename = input("Enter the file name (without extension): ")
f = FileHandler(filename)

choice = 0

while True:
    print("\nChoose an option:\n1. Write\n2. Append\n3. Read\n4. Exit")
    choice = input("Enter your choice: ")

    if choice == 1:
        text = input("Enter text to write in file: ")
        f.write_file(text)
    elif choice == 2:
        text = input("Enter text to append in file: ")
        f.append_file(text)
    elif choice == 3:
        f.read_file()
    elif choice == 4:
        print("\nExiting program. Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")
