s = input("Enter a string: ")
letters = sum(c.isalpha() for c in s)
digits = sum(c.isdigit() for c in s)

print(f"Alphabets: {letters} & Number: {digits}")
