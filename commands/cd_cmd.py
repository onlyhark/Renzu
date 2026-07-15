import os


def change_directory(path):
    if not path:
        print("Usage: cd <directory>")
        return

    try:
        os.chdir(path)
        print(f"Current directory: {os.getcwd()}")

    except FileNotFoundError:
        print("Directory not found.")

    except Exception as e:
        print(f"Error: {e}")