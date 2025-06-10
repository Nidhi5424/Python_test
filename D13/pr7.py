
class FileAnalyzer:
    def __init__(self, filename):
        self.filename = filename

    def analyze(self):
        with open(self.filename, 'r') as f:
            lines = f.readlines()
        print("Lines:", len(lines))
        print("Words:", sum(len(line.split()) for line in lines))
        print("Characters:", sum(len(line) for line in lines))

if __name__ == "__main__":
    analyzer = FileAnalyzer("sample.txt")
    analyzer.analyze()
