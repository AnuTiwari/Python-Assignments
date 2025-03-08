from collections import Counter

lst = list(map(int, input("Enter list elements: ").split()))
freq = Counter(lst)

print("Frequency count:", dict(freq))
