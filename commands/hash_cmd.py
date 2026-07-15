import hashlib
import os


def calculate_hash(filepath):
    if not os.path.exists(filepath):
        print("File not found.")
        return

    md5 = hashlib.md5()
    sha1 = hashlib.sha1()
    sha256 = hashlib.sha256()

    with open(filepath, "rb") as file:
        while chunk := file.read(4096):
            md5.update(chunk)
            sha1.update(chunk)
            sha256.update(chunk)

    print("\n=== HASH RESULTS ===")
    print(f"MD5    : {md5.hexdigest()}")
    print(f"SHA1   : {sha1.hexdigest()}")
    print(f"SHA256 : {sha256.hexdigest()}\n")