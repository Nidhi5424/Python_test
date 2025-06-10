
class BinaryReader:
    def __init__(self, filename):
        self.filename = filename

    def read_binary(self):
        with open(self.filename, 'rb') as f:
            content = f.read()
            print("Binary Content:\n", content)

if __name__ == "__main__":
    reader = BinaryReader("sample.txt")
    reader.read_binary()
