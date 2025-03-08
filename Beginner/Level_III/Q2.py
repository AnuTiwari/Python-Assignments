import os

base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, "demo.txt")

with open(file_path, "r") as file:
    line_count = sum(1 for line in file)

print(f"Total number of lines: {line_count}")
