start, stop = map(int, input("Enter start and stop values: ").split())

odd_sum = sum(i for i in range(start, stop + 1) if i % 2 != 0)
print(f"Sum of odd numbers: {odd_sum}")