def pf(n, d=2):    
    if n == 1:
        return []
    if n % d == 0:
        return [d] + pf(n // d, d)
    return pf(n, d+1)
num = int(input("Enter a positive integer: "))
factors = pf(num)
print(f"Prime factors of {num}: {factors}")
    


