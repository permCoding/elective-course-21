# https://kpolyakov.spb.ru/school/ege/gen.php?action=viewVar&answers=on&varId=1
# 2649
import math

f = open('26-s2.txt')
lines = f.read().split('\n')
f.close()

n = int(lines[0])
lst = list(reversed(sorted(map(int, lines[1:n+1]))))

a = lst[:n//2]
b = lst[n//2:]


# for i in range(0, n//2):
#     print(a[i], b[i])

s1 = sum(a)
s2 = sum(map(lambda e: e*0.8, filter(lambda x: x > 150, b)))
s3 = sum(filter(lambda x: x <= 150, b))

print(s1 + math.ceil(s2) + s3)
print(b[0])

