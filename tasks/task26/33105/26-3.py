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

maxe = 0
summ = sum(b)
a = sorted(a)

for i in range(len(a)):
    if i < len(a)//2:
        summ += a[i]*0.7
        maxe = a[i]
    else:
        summ += a[i]

print(math.ceil(summ), maxe)