def get(a, b):
    if a == b: return 1
    if a > b: return 0
    if a == 33: return 0 # с избегаемым этапом 
    r1 = get(a+1, b)
    r2 = get(a*2, b)
    r3 = get(a*3, b)
    return r1 + r2 + r3

print(get(3, 15) * get(15, 50)) # с обязательным этапом 15

'''
15+
33-

1. Прибавить 1
2. Умножить на 2
3. Умножить на 3
get(3, 9)
    111111
    2111
    3
    121
'''