import os

from commands.help_cmd import show_help
from commands.hash_cmd import calculate_hash
from commands.fileinfo_cmd import file_info
from commands.strings_cmd import extract_strings
from commands.scan_cmd import scan_file
from commands.exif_cmd import show_exif
from commands.interesting_cmd import interesting
from commands.hex_cmd import hex_dump
from commands.entropy_cmd import calculate_entropy
from commands.magic_cmd import detect_magic
from commands.peinfo_cmd import pe_info
from commands.cd_cmd import change_directory
from commands.pwd_cmd import show_pwd
from commands.ls_cmd import list_directory
from commands.imports_cmd import show_imports
from commands.cat_cmd import show_file


print("RENZU v0.1")
print("Digital Forensics & CTF Assistant")
print("Type 'help' for commands.\n")

while True:
    user_input = input("renzu> ").strip()
    parts = user_input.split(maxsplit=1)
    command = parts[0].lower() if parts else ""
    argument = parts[1] if len(parts) > 1 else ""

    if command == "help":
        show_help()

    elif command == "hash":
        calculate_hash(argument)

    elif command == "fileinfo":
        file_info(argument)

    elif command == "exit":
        print("Closing Renzu...")
        break

    elif command == "strings":
        extract_strings(argument)

    elif command == "scan":
        scan_file(argument)

    elif command == "exif":
        show_exif(argument)

    elif command == "interesting":
        interesting(argument)

    elif command == "hex":
        hex_dump(argument)

    elif command == "entropy":
        calculate_entropy(argument)

    elif command == "magic":
        detect_magic(argument)

    elif command == "peinfo":
        pe_info(argument)

    elif command == "cd":
        change_directory(argument)

    elif command == "pwd":
        show_pwd()

    elif command == "ls":
        list_directory()

    elif command in ["clear", "cls"]:
        os.system("cls" if os.name == "nt" else "clear")

    elif command == "imports":
        show_imports(argument)

    elif command == "cat":
        show_file(argument)

    else:
        print(f"Unknown command: {command}")