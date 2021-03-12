def F(x, k):
    if k < 0:
        return 0
    else:
        return (11 - k) * x ** k + F(x, k-1)


x = 2
k = 10
print(F(x, k))
