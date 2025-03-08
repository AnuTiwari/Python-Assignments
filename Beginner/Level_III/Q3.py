import os

def JtoI():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, "words.txt")

    with open(file_path, "r") as file:
        content = file.read()

    corrected_content = content.replace("J", "I")
    print(corrected_content)

JtoI()
