# A 784594 12
# B 8819088760 21

f = open('27_A.txt')
n = int(f.readline())
s = 0
dif = 10000000001
for i in range(n):
    lst = sorted(map(int, f.readline().split()))
    s += lst[2]
    r1 = lst[2] - lst[1]
    r0 = lst[2] - lst[0]
    if r1 % 109 != 0 and r1 < dif:
        dif = r1
    if r0 % 109 != 0 and r0 < dif:
        dif = r0

f.close()

print(dif)
print(s, s%109)
if s%109!=0:
    print(s, s%109)
else:
    s -= dif
    print(s, s%109)
