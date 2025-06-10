class MultiLineWriter:
    def __init__(self, filename):
        self.filename = filename

    def write_lines(self, lines):
        with open(self.filename, 'w') as file:
            for line in lines:
                file.write(line + "\n")
        print("Lines written to file.")

if __name__ == "__main__":
    content = [
        "Line 1: Python is easy to learn.",
        "Line 2: It has numerous libraries.",
        "Line 3: File handling is one of its features."
    ]
    writer = MultiLineWriter("notes.txt")
    writer.write_lines(content)
