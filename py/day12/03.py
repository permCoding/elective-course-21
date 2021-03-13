def F(x, p):
    if p < 0:
        return 0
    else:
        return (11-p)*x**p + F(x, p-1)


x = 1; p = 10
print(F(x, p))
