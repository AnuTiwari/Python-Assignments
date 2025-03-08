def run_length_encoding(s):
    if not s:
        return ""

    encoded = ""
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            encoded += s[i-1] + str(count)
            count = 1

    # Append the last character and its count
    encoded += s[-1] + str(count)
    
    return encoded

def main():
    input_string = input("Enter a string for Run-Length Encoding: ").strip()

    if not input_string:
        print("Invalid input! The string cannot be empty.")
        return

    encoded_string = run_length_encoding(input_string)

    print("\nEncoded String:")
    print(encoded_string)

if __name__ == "__main__":
    main()
