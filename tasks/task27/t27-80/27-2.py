# https://inf-ege.sdamgia.ru/problem?id=28130
# при вводе данных из файла A ответ — 3, из файла B — 625350

m = 80
b = 50
arr0 = [0] * m  # остатки для чисел <= 50
arr1 = [0] * m  # остатки для чисел > 50

with open('28130_B.txt') as f:
    n = int(f.readline())
    for _ in range(n):
        x = int(f.readline())
        t = x % m
        if x <= b:
            arr0[t] += 1
        else:
            arr1[t] += 1

res = 0
for i in range(1, m//2):
    res += arr1[i]*arr1[m-i]
    res += arr1[i]*arr0[m-i]
    res += arr0[i]*arr1[m-i]

res += arr1[0]*arr0[0]  # для остатка 0
res += arr1[0]*(arr1[0]-1)//2  # для остатка 0

res += arr1[40]*arr0[40]  # для остатка 40
res += arr1[40]*(arr1[40]-1)//2  # для остатка 40

print(res)

