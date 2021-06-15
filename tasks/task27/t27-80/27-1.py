# https://inf-ege.sdamgia.ru/problem?id=28130
# при вводе данных из файла A ответ — 3, из файла B — 625350

import time

start = time.monotonic()

m = 80
b = 50

with open('28130_B.txt') as f:
    n = int(f.readline())
    nums = list(map(int, f.readlines()))

k = 0
for i in range(n):
    for j in range(i+1, n):
        if nums[i] > b or nums[j] > b:
            if (nums[i] + nums[j]) % m == 0:
                k += 1

print(k)

finish = time.monotonic()
print(f'{round(finish - start, 2)} сек')
