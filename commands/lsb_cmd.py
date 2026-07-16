from PIL import Image
import os


def extract_lsb(args):
    if len(args) < 2:
        print("Usage:")
        print("lsb <image> red")
        print("lsb <image> green")
        print("lsb <image> blue")
        print("lsb <image> <0-7>")
        return

    filepath = args[0]
    mode = args[1].lower()

    if not os.path.exists(filepath):
        print("File not found.")
        return

    try:
        img = Image.open(filepath).convert("RGB")
        width, height = img.size

        output = Image.new("RGB", (width, height))

        for x in range(width):
            for y in range(height):
                r, g, b = img.getpixel((x, y))

                # RGB channel extraction
                if mode == "red":
                    value = 255 if (r & 1) else 0
                    output.putpixel((x, y), (value, value, value))

                elif mode == "green":
                    value = 255 if (g & 1) else 0
                    output.putpixel((x, y), (value, value, value))

                elif mode == "blue":
                    value = 255 if (b & 1) else 0
                    output.putpixel((x, y), (value, value, value))

                # Bitplane extraction
                elif mode.isdigit() and 0 <= int(mode) <= 7:
                    bit = int(mode)

                    rr = 255 if ((r >> bit) & 1) else 0
                    gg = 255 if ((g >> bit) & 1) else 0
                    bb = 255 if ((b >> bit) & 1) else 0

                    output.putpixel((x, y), (rr, gg, bb))

                else:
                    print("Invalid mode.")
                    return

        output_name = f"lsb_{mode}.png"
        output.save(output_name)

        print("\nLSB extraction completed.")
        print(f"Saved as: {output_name}")

    except Exception as e:
        print(f"Error: {e}")
