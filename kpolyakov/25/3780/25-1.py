'''3780
Найдите все натуральные числа, принадлежащие отрезку [63 000 000; 75 000 000], 
у которых ровно пять различных нечётных делителей (количество чётных делителей может быть любым). 
В ответе перечислите найденные числа, справа от каждого числа запишите его наибольший нечётный делитель.
'''
def check(x):
    k = 0
    d = 0
    for j in range(1, x+1, 2):
        if x%j == 0:
            k += 1
            d = j
        if k > 5:
            return 0
    if k < 5:
        return 0
    return d

s = 0
# 63123848
# 63 000 000
for i in range(63123847, 75000000):
    d = check(i)
    if d > 0:
        print(i, d)

# этот вариант работает слишком долго
