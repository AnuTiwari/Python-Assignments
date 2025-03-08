temps = list(map(int, input("Enter temperature readings: ").split()))

print(f"Average Temperature: {sum(temps)/len(temps):.2f}")
print(f"Highest Temperature: {max(temps)}")
print(f"Lowest Temperature: {min(temps)}")
