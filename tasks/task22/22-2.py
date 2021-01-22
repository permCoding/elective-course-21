'''
https://inf-ege.sdamgia.ru/problem?id=9655
Получив на вход число x, этот алгоритм печатает два числа: a и b. 
Укажите наименьшее из таких чисел x, при вводе которых 
алгоритм печатает сначала 48, а потом 6.
246
'''

for w in range(1, 500):
    # x = int(input())
    x = w
    a = 1
    b = 0
    while x > 0:
        c = x % 10
        a = a*c
        if c > b:
            b = c
        x //= 10
    if a == 48 and b == 6:
        print(w, a, b)