# https://inf-ege.sdamgia.ru/problem?id=27858

def get(x):
    k = 2 # 1 и сам x
    for i in range(2, x):
        if x%i == 0:
            k += 1
    return k

dmax = 0; nmax = 0
for n in range(120115, 120200+1):
    tmp = get(n)
    if tmp > dmax:
        dmax = tmp
        nmax = n
print(dmax, nmax)