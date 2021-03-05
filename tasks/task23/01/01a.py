# https://inf-ege.sdamgia.ru/problem?id=15959

def get(a, b):
    if a == b: return 1
    if a > b: return 0
    if a == 33: return 0
    r1 = get(a+1, b)
    r2 = get(a*2, b)
    r3 = get(a*3, b)
    return r1 + r2 + r3

print(get(3, 15) * get(15, 50))
print(get(3, 15))
print(get(15, 50))

# 11 * 11 = 121

'''
6 ?
- 5+1
- 3*2
- 2*3
'''
