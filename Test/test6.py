
from datetime import datetime

class JournalManager:
    def __init__(self):
        self.filename = "journal.txt"

    def add_entry(self, entry):
        date_time = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
        with open(self.filename, "a") as file:
            file.write(f"{date_time}\n{entry}\n\n")
        print("\nEntry added successfully!")

    def view_entries(self):
        try:
            with open(self.filename, "r") as file:
                content = file.read().strip()
                if content:
                    print("\nYour Journal Entries:\n------------------------------")
                    print(content)
                else:
                    print("\nNo journal entries found. Start by adding a new entry!")
        except FileNotFoundError:
            print("\nError: The journal file does not exist. Please add a new entry first.")

    def search_entries(self, keyword):
        try:
            with open(self.filename, "r") as file:
                entries = file.read().strip().split("\n\n")
                found = False
                for entry in entries:
                    if keyword.lower() in entry.lower():
                        if not found:
                            print("\nMatching Entries:\n------------------------------")
                            found = True
                        print(entry + "\n")
                if not found:
                    print(f"\nNo entries were found for the keyword: {keyword}.")
        except FileNotFoundError:
            print("\nError: The journal file does not exist. Please add a new entry first.")

    def delete_entries(self):
        import os
        if os.path.exists(self.filename):
            confirm = input("\nAre you sure you want to delete all entries? (yes/no): ").strip().lower()
            if confirm == "yes":
                os.remove(self.filename)
                print("\nAll journal entries have been deleted.")
            else:
                print("\nDeletion cancelled.")
        else:
            print("\nNo journal entries to delete.")


journal = JournalManager()

while True:
    print("""
Welcome to Personal Journal Manager!
Please select an option:
1. Add a New Entry
2. View All Entries
3. Search for an Entry
4. Delete All Entries
5. Exit
""")
    try:
        choice = int(input("User Input: ").strip())
    except ValueError:
        choice = 0

    match choice:
        case 1:
            entry = input("\nEnter your journal entry:\n")
            journal.add_entry(entry)

        case 2:
            journal.view_entries()

        case 3:
            keyword = input("\nEnter a keyword or date to search: ")
            journal.search_entries(keyword)

        case 4:
            journal.delete_entries()

        case 5:
            print("\nThank you for using Personal Journal Manager. Goodbye!")
            break

        case _:
            print("\nInvalid option. Please select a valid option from the menu.")
