
class FileCopier:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

    def copy(self):
        with open(self.source, 'r') as src, open(self.destination, 'w') as dest:
            dest.write(src.read())
        print("File copied successfully.")

if __name__ == "__main__":
    copier = FileCopier("source.txt", "backup.txt")
    copier.copy()
