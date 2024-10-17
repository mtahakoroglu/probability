import math

def comb(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

x = comb(15, 2) * comb(10, 3) / comb(25, 5)

print(f"{x:.3f}")