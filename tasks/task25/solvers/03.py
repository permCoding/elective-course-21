'''
https://inf-ege.sdamgia.ru/problem?id=27858
Напишите программу, которая ищет среди целых чисел, 
принадлежащих числовому отрезку [120115; 120200], 
число, имеющее максимальное количество различных 
натуральных делителей, если таких чисел несколько — 
найдите максимальное из них. Выведите на экран 
количество делителей такого числа и само число.
'''

def get(x):
    k = 0
    for i in range(1, x+1):
        if x%i == 0:
            k += 1
    return k

d = 0; z = 0
for x in range(120115, 120200+1):
    t = get(x)
    if t >= d:
        d = t
        z = x
print(get(z),z)