import os
from datetime import datetime


def file_info(filepath):
    if not os.path.exists(filepath):
        print("File not found.")
        return

    size = os.path.getsize(filepath)

    created = datetime.fromtimestamp(
        os.path.getctime(filepath)
    )

    modified = datetime.fromtimestamp(
        os.path.getmtime(filepath)
    )

    extension = os.path.splitext(filepath)[1]

    print("\n=== FILE INFORMATION ===")
    print(f"Name      : {os.path.basename(filepath)}")
    print(f"Size      : {size} bytes")
    print(f"Extension : {extension}")
    print(f"Created   : {created}")
    print(f"Modified  : {modified}")
    print()