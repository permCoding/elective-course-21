# задача 16 из Демо
def F(n):
    if n == 1: return 1
    if n%2 == 0: return n + F(n-1)
    return 2 * F(n - 2)
    # если n > 1 и при этом n – нечётно.

print(F(26))