'''3780
Найдите все натуральные числа, принадлежащие отрезку [63 000 000; 75 000 000], 
у которых ровно пять различных нечётных делителей (количество чётных делителей может быть любым). 
В ответе перечислите найденные числа, справа от каждого числа запишите его наибольший нечётный делитель.
'''
def check(x):
    lst = []
    for j in range(1, int(x**.5)+1):
        if x%j == 0:
            if j%2 != 0:
                lst.append(j)
            if (x//j)%2 != 0 and x//j != j:
                lst.append(x//j)
        if len(lst) > 5:
            return 0
    if len(lst) < 5:
        return 0
    return max(lst)

# 63123848 7890481
# 63 000 000
for i in range(63123848, 65000000):
    t = check(i)
    if t > 0:
        print(i, t)

# этот вариант работает слишком долго
