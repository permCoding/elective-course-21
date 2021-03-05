# https://inf-ege.sdamgia.ru/problem?id=11358

def get(a, b):
    if b < a: return 0
    if b == a: return 1
    r1 = get(a, b-1)
    r2 = get(a, b-2)
    r3 = get(a, b//2) if b%2 == 0 else 0
    return r1 + r2 + r3


print(get(3, 10) * get(10, 12))
