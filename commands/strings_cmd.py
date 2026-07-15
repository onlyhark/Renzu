import os
import re


def extract_strings(filepath, min_length=4):
    if not os.path.exists(filepath):
        print("File not found.")
        return

    with open(filepath, "rb") as file:
        data = file.read()

    pattern = rb"[\x20-\x7E]{" + str(min_length).encode() + rb",}"

    matches = re.findall(pattern, data)

    print("\n=== STRINGS OUTPUT ===\n")

    for match in matches:
        try:
            print(match.decode())
        except:
            pass

    print()