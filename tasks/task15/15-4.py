# https://inf-ege.sdamgia.ru/problem?id=7763
'''
На числовой прямой даны два отрезка: P = [5, 30] и Q = [14, 23].
Укажите наибольшую возможную длину промежутка A, для которого формула
    ((x ∈ P) ≡ (x ∈ Q)) → ¬(x ∈ A)
тождественно истинна, т.е. =1 при любом значении переменной х.
'''


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


# # эта часть просто для проверки
# AL = 5
# AR = 13
# check = True
# for x in range(-100, 100):
#     if get(x, AL, AR) is False:
#         check = False
#         break
# if check is True:
#     mx = AR - AL + 1
#     print(mx)
