f = open('27-A.txt')
n = int(f.readline())

result = 0; dif = 10001
for _ in range(n):
    line = f.readline()
    a, b = map(int, line.split())
    result += max(a, b)
    if abs(a - b) < dif and abs(a - b) % 3 != 0:
        dif = abs(a - b)

if result % 3 != 0:
    print(result)
else:
    print(result - dif)
