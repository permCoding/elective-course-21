# https://kpolyakov.spb.ru/school/ege/gen.php?action=viewVar&answers=on&varId=1
'''
№ 2260 
Обозначим через ДЕЛ(n, m) утверждение «натуральное число n делится без остатка на натуральное число m». 
Для какого наименьшего натурального числа А формула
(ДЕЛ(x, A) ∧ ДЕЛ(x, 24) ∧ ¬ДЕЛ(x, 16)) → ¬ДЕЛ(x, A)
тождественно истинна (то есть принимает значение 1 при любом натуральном значении переменной х)?
'''


def dl(n, m):
    return not(bool(n % m))


def get(x, A):
    f = dl(x, A) and dl(x, 24) and not(dl(x, 16))
    return int(f) <= int(not(dl(x, A)))


for A in range(1, 1000):
    check = True
    for x in range(1, 1000):
        if get(x, A) is False:
            check = False
            break
    if check is True:
        print(A)
        break

print('- - -')

