import os


def list_directory():
    current_dir = os.getcwd()

    try:
        items = os.listdir(current_dir)

        if not items:
            print("Directory is empty.")
            return

        for item in items:
            full_path = os.path.join(current_dir, item)

            if os.path.isdir(full_path):
                print(f"[DIR]  {item}")
            else:
                print(f"[FILE] {item}")

    except Exception as e:
        print(f"Error: {e}")