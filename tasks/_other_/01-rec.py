def F(x, n, k, z=0):
    if k == 0:
        return 0
    else:
        z += x**k
        return n/z + F(x, n, k-1, z)


n = 2
x = 2
print(F(x, n, n))
