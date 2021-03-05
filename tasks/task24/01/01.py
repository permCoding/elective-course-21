# https://inf-ege.sdamgia.ru/problem?id=29672

f = open('inf_22_10_20_24.txt')
lines = f.readlines()
f.close()

k = 0

for line in lines:
    if line.count('E') > line.count('A'):
        k += 1

print(k)

