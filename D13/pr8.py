
class ReadWriteModifier:
    def __init__(self, filename):
        self.filename = filename

    def modify(self):
        with open(self.filename, 'r+') as f:
            content = f.read()
            print("Old Content:\n", content)
            f.write("\nThis file was last modified by adding this sentence.")

if __name__ == "__main__":
    modifier = ReadWriteModifier("sample.txt")
    modifier.modify()
