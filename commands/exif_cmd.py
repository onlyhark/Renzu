import subprocess
import json
import os


def show_exif(file_path):
    if not file_path:
        print("Usage: exif <image_path>")
        return

    if not os.path.exists(file_path):
        print("[-] File not found.")
        return

    try:
        result = subprocess.run(
            ["exiftool", "-j", file_path],
            capture_output=True,
            text=True,
            check=True
        )

        metadata = json.loads(result.stdout)[0]

        print("=" * 70)
        print("                    RENZU EXIF ANALYSIS")
        print("=" * 70)

        important_fields = [
            "FileName",
            "Directory",
            "FileSize",
            "FileType",
            "FileTypeExtension",
            "MIMEType",

            "ImageWidth",
            "ImageHeight",

            "Artist",
            "Author",
            "Creator",

            "Comment",
            "UserComment",
            "XPComment",

            "ImageDescription",
            "Description",
            "Caption-Abstract",

            "XPTitle",
            "XPSubject",
            "XPKeywords",

            "Copyright",

            "Software",

            "CreateDate",
            "ModifyDate",
            "DateTimeOriginal",

            "Make",
            "Model",

            "GPSLatitude",
            "GPSLongitude",

            "Keywords"
        ]

        print("\n[ Important Metadata ]\n")

        for field in important_fields:
            print(f"{field:<25}: {metadata.get(field, 'Not Found')}")

        print("\n" + "=" * 70)
        print("                    ALL METADATA")
        print("=" * 70)

        for key in sorted(metadata.keys()):
            print(f"{key:<35}: {metadata[key]}")

    except FileNotFoundError:
        print("[-] ExifTool is not installed or not in PATH.")

    except subprocess.CalledProcessError:
        print("[-] ExifTool failed to read metadata.")

    except Exception as e:
        print(f"[-] {e}")
