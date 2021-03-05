# https://inf-ege.sdamgia.ru/problem?id=14708

def get(a, b):
    if a > b: return 0
    if a == b: return 1
    return get(a+1, b) + get(a*2, b)


print(get(1, 10) * get(10, 21) * get(21, 30))
