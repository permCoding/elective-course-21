# https://inf-ege.sdamgia.ru/problem?id=15959

def get(a, b):
    if b == 33: return 0
    if a == b: return 1
    r1 = 0 if b-1 < a else get(a, b-1)
    r2 = 0 if b%2 != 0 or b//2 < a else get(a, b//2)
    r3 = 0 if b%3 != 0 or b//3 < a else get(a, b//3)
    return r1 + r2 + r3

print(get(3, 15) * get(15, 50))



'''
6 ?
- 5+1
- 3*2
- 2*3
'''
