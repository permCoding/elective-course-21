import math

f = open('inf_22_10_20_26.txt')
# f = open('26test.txt')
n = int(f.readline())
a = []
b = []
for _ in range(n):
    k = int(f.readline())
    if k > 100:
        a.append(k)
    else:
        b.append(k)

a = sorted(a)
summ = sum(a[n//2:])+sum(b)
for e in a[:n//2]:
    if e > 100:
        summ += e*0.7
    else:
        summ += e
    m = e

print(math.ceil(summ),m)