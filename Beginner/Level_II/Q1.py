l1 = list(map(int, input("Enter elements of list 1: ").split()))
l2 = list(map(int, input("Enter elements of list 2: ").split()))

common_elements = list(set(l1) & set(l2))
print(f"Common elements: {common_elements}")
