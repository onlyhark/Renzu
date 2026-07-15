import os
import re


def interesting(filepath):
    if not os.path.exists(filepath):
        print("File not found.")
        return

    with open(filepath, "rb") as file:
        data = file.read()

    text = data.decode(errors="ignore")

    try:
        text = data.decode(errors="ignore")
    except:
        print("Unable to decode file.")
        return

    urls = re.findall(r'https?://[^\s"]+', text)
    ips = re.findall(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', text)
    emails = re.findall(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}', text)
    flags = re.findall(r'(?i)(?:flag|ctf)\{.*?\}', text)
    passwords = re.findall(r'(?i)(?:password|passwd|token)\s*[:=]\s*\S+', text)

    print("\n========== INTERESTING FINDINGS ==========\n")

    if urls:
        print("[URL]")
        for item in urls:
            print(item)
        print()

    if ips:
        print("[IP]")
        for item in ips:
            print(item)
        print()

    if emails:
        print("[EMAIL]")
        for item in emails:
            print(item)
        print()

    if flags:
        print("[FLAG]")
        for item in flags:
            print(item)
        print()

    if passwords:
        print("[PASSWORD]")
        for item in passwords:
            print(item)
        print()