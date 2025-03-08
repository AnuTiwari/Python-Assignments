def JtoI():
    with open("words.txt", "r") as file:
        content = file.read()

    corrected_content = content.replace("J", "I")
    print(corrected_content)

JtoI()
