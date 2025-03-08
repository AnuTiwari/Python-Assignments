lst = list(map(int, input("Enter list elements: ").split()))
index = int(input("Enter index to access: "))

try:
    print(lst[index])
except IndexError:
    print("Error: Index out of range!")
