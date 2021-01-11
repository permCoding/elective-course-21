# https://inf-ege.sdamgia.ru/problem?id=7929
'''
Элементами множеств А, P, Q являются натуральные числа, причём
P = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20},
Q = {3, 6, 9, 12, 15, 18, 21, 24, 27, 30}.
Известно, что выражение
    ( (x ∈ A) → (x ∈ P) ) ∧ ( (x ∈ Q) → ¬(x ∈ A) )
истинно (т.е. = 1) при любом значении переменной х.
Определите наибольшее возможное количество элементов в множестве A.
'''

# этот кусок кода просто для проверки
# x = 3
# f = x in {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
# print(f)
# f = x in [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# print(f)

# этот кусок кода просто для проверки
# P = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
# Q = {3, 6, 9, 12, 15, 18, 21, 24, 27, 30}
# A = P | Q
# print(len(A))
# print(A)


# программный код нужно переписать - он от другой задачи

P = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
Q = {3, 6, 9, 12, 15, 18, 21, 24, 27, 30}
A = P | Q

def get(x, B):
    f1 = x in P
    f2 = x in Q
    f3 = x in B
    return (int(f3) <= int(f1)) and (int(f2) <= int(not(f3)))


mx = 0
DL = +1
DR = +31
lst = list(A)
for num in range(0, 2**len(A)):
    B = []
    bn = num
    pos = 0
    while bn > 0:
        if bn & 1 > 0:
            B.append(lst[pos])
        pos += 1
        bn >>= 1
    check = True
    for x in range(DL, DR):
        if get(x, B) is False:
            check = False
            break
    if check is True:
        if len(B) > mx: # нужно выбрать самый большой
            mx = len(B)


print(f'mx = {mx}')

