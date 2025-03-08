arr = list(map(int, input("Enter list elements: ").split()))
k = int(input("Enter value of k: "))

count = sum(1 for i in range(len(arr)) for j in range(i + 1, len(arr)) if arr[i] + arr[j] == k)
print(f"Pair count: {count}")
