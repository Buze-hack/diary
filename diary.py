import os
from datetime import datetime

def main():
    while True:
        print("Welcome to your diary!")
        print("1. Write a new entry")
        print("2. View entries")
        print("3. Exit")

        choice = input("choose an option (1-3): ").strip()

        if choice == '1':
            add_entry()
        elif choice == '2':
            view_entries()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

def add_entry():
    print("\nEnter your diary entry (type 'exit' to finish):")

    lines = []
    while True:
        line = input()
        if line.strip().lower() == 'exit':
            break
        lines.append(line)

    entry_text = "\n".join(lines)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("diary.txt", "a") as diary_file:
        diary_file.write(f"\n---{timestamp}---\n")
        diary_file.write(entry_text + "\n")
        diary_file.write("-" * 40 + "\n")

    print("Entry saved successfully!\n")


def view_entries():
    print("\nYour diary entries:")

    if not os.path.exists("diary.txt"):
        print("No entries found.")
        return
    
    with open("diary.txt", "r") as diary_file:
        content = diary_file.read()

    if content.strip() == "":
        print("No entries found.")
    else:
        print(content)

if __name__ == "__main__":
    main()