import os

MAGIC_SIGNATURES = {
    b"\x89PNG\r\n\x1a\n": "PNG Image",
    b"\xff\xd8\xff": "JPEG Image",
    b"GIF87a": "GIF Image",
    b"GIF89a": "GIF Image",

    b"%PDF": "PDF Document",

    b"PK\x03\x04": "ZIP Archive",

    b"Rar!\x1A\x07\x00": "RAR Archive",
    b"7z\xBC\xAF\x27\x1C": "7-Zip Archive",

    b"MZ": "Windows Executable",

    b"\x7FELF": "ELF Executable",

    b"SQLite format 3\x00": "SQLite Database"
}

EXPECTED_EXTENSIONS = {
    "PNG Image": [".png"],
    "JPEG Image": [".jpg", ".jpeg"],
    "GIF Image": [".gif"],
    "PDF Document": [".pdf"],
    "ZIP Archive": [".zip"],
    "RAR Archive": [".rar"],
    "7-Zip Archive": [".7z"],
    "Windows Executable": [".exe", ".dll"],
    "ELF Executable": [".elf"],
    "SQLite Database": [".db", ".sqlite", ".sqlite3"]
}

def detect_magic(filepath):
    if not os.path.exists(filepath):
        print("File not found.")
        return

    with open(filepath, "rb") as file:
        header = file.read(32)

    detected = "Unknown"

    for signature, filetype in MAGIC_SIGNATURES.items():
        if header.startswith(signature):
            detected = filetype
            break

    extension = os.path.splitext(filepath)[1].lower()

    print("\n========== MAGIC ==========\n")
    print(f"Extension     : {extension if extension else 'None'}")
    print(f"Detected Type : {detected}")

    magic_bytes = " ".join(f"{byte:02X}" for byte in header[:8])
    print(f"Magic Bytes   : {magic_bytes}")

    if detected in EXPECTED_EXTENSIONS:
        if extension not in EXPECTED_EXTENSIONS[detected]:
            print("\n[WARNING]")
            print("File extension does not match detected file type.")
            print("Possible renamed, hidden or embedded file.")

    print()
