# https://kpolyakov.spb.ru/school/ege/gen.php?action=viewVar&answers=on&varId=1
# 2649
import math

f = open('26-s2.txt')
lines = f.read().split('\n')
f.close()

n = int(lines[0])
lst = list(reversed(sorted(map(int, lines[1:n+1]))))

w1 = list(filter(lambda x: x > 150, lst))
w2 = list(filter(lambda x: x <= 150, lst))
# for i in range(0, n//2):
#     print(a[i], b[i])

n = len(w1)

a = lst[:(n+1)//2]
b = lst[(n+1)//2:]

s1 = sum(a)
s2 = sum(map(lambda e: math.ceil(e*0.8), b))
s3 = sum(w2)

print(s1 + s2 + s3)
print(b[0])

