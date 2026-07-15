import os


def hex_dump(filepath, bytes_per_line=16):
    if not os.path.exists(filepath):
        print("File not found.")
        return

    with open(filepath, "rb") as file:
        offset = 0

        while chunk := file.read(bytes_per_line):
            hex_values = " ".join(f"{byte:02X}" for byte in chunk)

            ascii_values = "".join(
                chr(byte) if 32 <= byte <= 126 else "."
                for byte in chunk
            )

            print(
                f"{offset:08X}  "
                f"{hex_values:<48}  "
                f"{ascii_values}"
            )

            offset += bytes_per_line