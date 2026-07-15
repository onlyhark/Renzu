import os


def show_file(filepath):
    if not filepath:
        print("Usage: cat <file>")
        return

    if not os.path.exists(filepath):
        print("File not found.")
        return

    if os.path.isdir(filepath):
        print("Cannot read a directory.")
        return

    try:
        with open(filepath, "r", encoding="utf-8") as file:
            content = file.read()

        print("\n========== FILE CONTENT ==========\n")
        print(content)

    except UnicodeDecodeError:
        print("This file is not a text file.")

    except Exception as e:
        print(f"Error: {e}")