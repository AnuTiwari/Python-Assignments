def count_customers_left(N, S):
    occupied = set()
    customers = {}
    left_count = 0

    for c in S:
        if c in customers:
            if customers[c]:  
                occupied.remove(c)
            del customers[c]
        else:
            if len(occupied) < N:
                occupied.add(c)
                customers[c] = True
            else:
                left_count += 1
                customers[c] = False

    return left_count

N = int(input("Enter number of computers: "))
S = input("Enter customer sequence: ")

print(f"Customers left without a computer: {count_customers_left(N, S)}")
