def F1(n):
    print(n**2)


def F2(n):
    return n**2


def F3(n):  # сумма чисел от 0 до n
    if n == 0:  # точка останова
        return 0
    else:  # шаг рекурсии
        return n + F3(n-1)


x = 10
F1(x)
print(F2(x))
print(F3(x))
