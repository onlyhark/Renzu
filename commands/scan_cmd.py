import os
from commands.hash_cmd import calculate_hash
from commands.fileinfo_cmd import file_info
from commands.strings_cmd import extract_strings


def scan_file(filepath):
    if not os.path.exists(filepath):
        print("File not found.")
        return

    print("\n========== RENZU SCAN ==========\n")

    print("[1/3] Gathering file information...")
    file_info(filepath)

    print("[2/3] Calculating hashes...")
    calculate_hash(filepath)

    print("[3/3] Extracting strings...")
    extract_strings(filepath)

    print("========== SCAN COMPLETED ==========\n")