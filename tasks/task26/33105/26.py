import math

f = open('inf_22_10_20_26.txt')
n = int(f.readline())
a = []
for _ in range(n):
    a.append(int(f.readline()))

a = sorted(a)
summ = sum(a[n//2:])
for e in a[:n//2]:
    if e > 100:
        summ += e*0.7
    else:
        summ += e
    m = e

print(math.ceil(summ),m)