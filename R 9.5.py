def power(a, b):
    if b == 0:
        return 1
    return a * power(a, b - 1) if b > 0 else 1 / power(a, -b)
a = int(input("Enter base value a: "))
b = int(input("Enter exponent value b: "))
result = power(a, b)
print(f"{a} raised to the power of {b} is {result}")