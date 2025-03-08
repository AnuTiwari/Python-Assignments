num = int(input("Enter a number: "))
divisors_sum = sum(i for i in range(1, num) if num % i == 0)

print("Yes" if divisors_sum == num else "No")
