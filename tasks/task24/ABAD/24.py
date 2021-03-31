# https://inf-ege.sdamgia.ru/problem?id=33196

import string
from functools import reduce

with open('24.txt') as f:
    line = f.readline()

d = {x: 0 for x in string.ascii_uppercase}
res = ('', 0)
for i in range(1, len(line)):
    d[line[i]] += 1 if line[i-1] == 'A' else 0
    if d[line[i]] > res[1]:
        res = (line[i], d[line[i]])

print(res)
