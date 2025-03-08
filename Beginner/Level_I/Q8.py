import math

num1, num2 = map(int, input("Enter two numbers: ").split())
lcm = abs(num1 * num2) // math.gcd(num1, num2)

print(f"LCM of {num1} and {num2} is: {lcm}")
