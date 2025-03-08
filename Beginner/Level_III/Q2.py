with open("demo.txt", "r") as file:
    line_count = sum(1 for line in file)

print(f"Total number of lines: {line_count}")
