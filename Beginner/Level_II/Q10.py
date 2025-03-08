n = int(input("Enter number of stones: "))
stones = list(range(2, n+1, 2)) if n % 2 == 0 else list(range(1, n+1, 2))

print(f"Stones in a single pile: {stones}")
