def F2(n):
    if n == 0: # точка останова
        return 0
    else: # шаг рекурсии
        return n + F2(n-1)


n = 10
print(F2(n))




