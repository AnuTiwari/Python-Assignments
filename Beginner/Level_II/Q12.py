username = input("Set your username: ")
password = input("Set your password: ")

for attempt in range(3):
    u = input("Enter username: ")
    p = input("Enter password: ")

    if u == username and p == password:
        print("Login successful!")
        break
    else:
        print(f"Invalid credentials! {2 - attempt} attempts left.")

if attempt == 2:
    print("Too many failed attempts. Try again later.")
