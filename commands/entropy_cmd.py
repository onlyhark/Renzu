import math
import os
from collections import Counter


def calculate_entropy(filepath):
    if not os.path.exists(filepath):
        print("File not found.")
        return

    with open(filepath, "rb") as file:
        data = file.read()

    if len(data) == 0:
        print("Empty file.")
        return

    counter = Counter(data)

    entropy = 0

    for count in counter.values():
        probability = count / len(data)
        entropy -= probability * math.log2(probability)

    print("\n========== ENTROPY ==========")
    print(f"Entropy: {entropy:.4f}")

    if entropy < 4:
        print("Assessment: Low entropy")
    elif entropy < 7:
        print("Assessment: Medium entropy")
    else:
        print("Assessment: High entropy")
        print("Possible compressed, packed or encrypted file.")

    print()