# https://inf-ege.sdamgia.ru/problem?id=11358

def get(a, b):
    if a > b: return 0
    if a == b: return 1
    return get(a+1, b) + get(a+2, b) + get(a*2, b)


print(get(3, 10) * get(10, 12))
