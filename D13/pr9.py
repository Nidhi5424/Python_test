
class WordSearcher:
    def __init__(self, filename):
        self.filename = filename

    def search_word(self, word):
        with open(self.filename, 'r') as f:
            lines = f.readlines()
        found = False
        for idx, line in enumerate(lines, 1):
            if word in line:
                print(f"'{word}' found on line {idx}")
                found = True
        if not found:
            print(f"'{word}' not found in file.")

if __name__ == "__main__":
    word = input("Enter word to search: ")
    searcher = WordSearcher("sample.txt")
    searcher.search_word(word)
