import os
import pefile


def pe_info(filepath):
    if not os.path.exists(filepath):
        print("File not found.")
        return

    try:
        pe = pefile.PE(filepath)

        print("\n========== PE INFO ==========\n")

        machine_types = {
            0x14C: "x86",
            0x8664: "x64",
            0x1C0: "ARM",
            0xAA64: "ARM64"
        }

        architecture = machine_types.get(
            pe.FILE_HEADER.Machine,
            hex(pe.FILE_HEADER.Machine)
        )

        print(f"Architecture : {architecture}")

        print(
            f"Entry Point  : "
            f"0x{pe.OPTIONAL_HEADER.AddressOfEntryPoint:X}"
        )

        print(
            f"Image Base   : "
            f"0x{pe.OPTIONAL_HEADER.ImageBase:X}"
        )

        print(
            f"Sections     : "
            f"{pe.FILE_HEADER.NumberOfSections}"
        )

        print("\nSections:")
        for section in pe.sections:
            print(
                f"  {section.Name.decode(errors='ignore').strip(chr(0))}"
            )

        if hasattr(pe, "DIRECTORY_ENTRY_IMPORT"):
            print("\nImported DLLs:")
            for entry in pe.DIRECTORY_ENTRY_IMPORT:
                print(
                    f"  {entry.dll.decode(errors='ignore')}"
                )

    except pefile.PEFormatError:
        print("This is not a valid PE file.")

    except Exception as e:
        print(f"Error: {e}")