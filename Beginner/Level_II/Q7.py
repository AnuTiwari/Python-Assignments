import statistics

numbers = list(map(int, input("Enter list elements: ").split()))
print(f"Median: {statistics.median(numbers)}")
