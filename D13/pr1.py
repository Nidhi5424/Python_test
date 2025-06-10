
class FileCreator:
    def __init__(self, filename):
        self.filename = filename

    def write(self, text):
        with open(self.filename, 'w') as f:
            f.write(text)

f1 = FileCreator("sample.txt")
f1.write("Python is a versatile programming language.")
