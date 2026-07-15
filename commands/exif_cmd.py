from PIL import Image
from PIL.ExifTags import TAGS
import os


def show_exif(filepath):
    if not os.path.exists(filepath):
        print("File not found.")
        return

    try:
        image = Image.open(filepath)

        exif_data = image.getexif()

        if not exif_data:
            print("No EXIF data found.")
            return

        print("\n========== EXIF DATA ==========\n")

        for tag_id, value in exif_data.items():
            tag = TAGS.get(tag_id, tag_id)
            print(f"{tag}: {value}")

        print()

    except Exception as e:
        print(f"Error: {e}")