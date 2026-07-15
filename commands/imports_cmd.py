import os
import pefile


def show_imports(filepath):
    if not os.path.exists(filepath):
        print("File not found.")
        return

    try:
        pe = pefile.PE(filepath)

        print("\n========== IMPORTS ==========\n")

        if not hasattr(pe, "DIRECTORY_ENTRY_IMPORT"):
            print("No imports found.")
            return

        for entry in pe.DIRECTORY_ENTRY_IMPORT:
            dll_name = entry.dll.decode(errors="ignore")

            print(f"[{dll_name}]")

            for imp in entry.imports:
                if imp.name:
                    print(f"  {imp.name.decode(errors='ignore')}")

            print()

    except pefile.PEFormatError:
        print("This is not a valid PE file.")

    except Exception as e:
        print(f"Error: {e}")