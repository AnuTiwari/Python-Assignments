def parse_string(encoded_str):
    parts = encoded_str.split("0")
    parts = [part for part in parts if part]
    return {"first_name": parts[0], "last_name": parts[1], "id": parts[2]}

encoded_str = "Robert000Smith000123"
print(parse_string(encoded_str))
