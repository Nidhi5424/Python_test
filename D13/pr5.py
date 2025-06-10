
class FileAppender:
    def __init__(self, filename):
        self.filename = filename

    def append_line(self, line):
        with open(self.filename, 'a') as f:
            f.write(line + '\n')
        print("Line appended.")

if __name__ == "__main__":
    f = FileAppender("notes.txt")
    f.append_line("Line 4: Python supports multiple modes of file handling.")
