def parse_string(encoded_str):
    # Split the input string by '0' and filter out empty strings
    parts = encoded_str.split("0")
    parts = [part for part in parts if part]  # Remove empty parts

    # Ensure we have exactly three parts (first name, last name, ID)
    if len(parts) != 3:
        print("Invalid input format! Ensure the string has a first name, last name, and ID separated by zeros.")
        return None

    return {"first_name": parts[0], "last_name": parts[1], "id": parts[2]}

def main():
    encoded_str = input("Enter the encoded string: ").strip()

    parsed_data = parse_string(encoded_str)
    if parsed_data:
        print("\nParsed Data:")
        print(parsed_data)

if __name__ == "__main__":
    main()
