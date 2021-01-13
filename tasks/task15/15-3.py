# https://inf-ege.sdamgia.ru/problem?id=14704
'''
Сколько существует целых значений числа A, при которых формула
((x < 6) → (x2 < A)) ∧ ((y2 ≤ A) → (y ≤ 6))
тождественно истинна при любых целых неотрицательных x и y?
'''


def get(x, y, A):
    return (int(x < 6) <= int(x**2 < A)) and (int(y**2 <= A) <= int(y <= 6))


count = 0
for A in range(-100, 100):
    check = True
    for x in range(0, 100):
        for y in range(0, 100):
            if get(x, y, A) == False:
                check = False
    if check:
        count += 1
        print(A)

print(f'count = {count}')
