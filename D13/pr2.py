class FileModifier:
    def __init__(self, filename):
        self.filename = filename

    def read_file(self):
        with open(self.filename, 'r') as file:
            print("Original Content:")
            print(file.read())

    def overwrite_file(self, new_content):
        with open(self.filename, 'w') as file:
            file.write(new_content)
        print("File content overwritten.")

if __name__ == "__main__":
    f = FileModifier("sample.txt")
    f.read_file()
    f.overwrite_file("Learning file handling in Python is fun!")
