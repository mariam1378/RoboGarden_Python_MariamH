import os

def write_entry(file_name):
    try:
        with open(file_name, "a") as file:
            print("\nWrite your diary entry (type 'END' on a new line to finish):")
            while True:
                line = input()
                if line.strip().upper() == "END":
                    break
                file.write(line + "\n")
            print("Your entry has been saved!")
    except PermissionError:
        print("Error: You do not have permission to write to this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def view_entries(file_name):
    try:
        if not os.path.exists(file_name):
            print("No entries found. Start by writing your first diary entry!")
            return
        with open(file_name, "r") as file:
            entries = file.readlines()
            if not entries:
                print("No entries found in the diary.")
                return
            print("\nYour previous diary entries:")
            print("-" * 30)
            for entry in entries:
                print(entry.strip())
            print("-" * 30)
    except PermissionError:
        print("Error: You do not have permission to read this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    file_name = "personal_diary.txt"
    while True:
        print("\n--- Personal Diary ---")
        print("1. Write a new entry")
        print("2. View previous entries")
        print("3. Exit")
        try:
            choice = int(input("Choose an option: "))
            if choice == 1:
                write_entry(file_name)
            elif choice == 2:
                view_entries(file_name)
            elif choice == 3:
                print("Goodbye! Your diary is safe.")
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
