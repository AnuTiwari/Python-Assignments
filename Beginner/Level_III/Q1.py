with open("doc.txt", "r") as file:
    words = file.read().split()

even_words = [word for word in words if len(word) % 2 == 0]
print("Even length words:", " ".join(even_words))
