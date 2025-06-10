class FileReader:
    def __init__(self, filename):
        self.filename = filename

    def read_lines(self):
        with open(self.filename, 'r') as file:
            for line in file:
                print(line.strip())

if __name__ == "__main__":
    f = FileReader("sample.txt")
    f.read_lines()