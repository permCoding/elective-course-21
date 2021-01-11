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

# программный код нужно переписать - он от другой задачи

def get(x, AL, AR):
    f1 = 5 <= x <= 30
    f2 = 14 <= x <= 23
    f3 = not(AL <= x <= AR)
    return int(f1 == f2) <= int(f3)


DL = -100
DR = +100
mx = 0 # ширина искомого участка
for AL in range(DL, DR):
    for AR in range(DL, DR):
        check = True
        for x in range(DL, DR):
            if get(x, AL, AR) is False:
                check = False
                break
        if check is True:
            if AR - AL + 1 > mx: # нужно выбрать самый большой
                mx = AR - AL + 1

print(f'mx = {mx}')
