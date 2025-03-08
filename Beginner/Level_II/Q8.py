s = input("Enter a string: ")
vowel_count = sum(1 for c in s.lower() if c in "aeiou")

print(f"Number of vowels: {vowel_count}")
