import os

# Get the correct absolute path
base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, "doc.txt")

with open(file_path, "r") as file:
    words = file.read().split()

even_words = [word for word in words if len(word) % 2 == 0]
print("Even length words:", " ".join(even_words))
