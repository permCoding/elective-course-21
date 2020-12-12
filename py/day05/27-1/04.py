f = open('27-C_demo.txt')
n = int(f.readline())

result = 0; dif = 823746918491842739           #
for _ in range(n):
    line = f.readline()
    a, b = map(int, line.split())
    result += max(a, b)
    if abs(a - b) < dif: dif = abs(a - b)
    # % 3

if result % 3 != 0:  # <> не равно
    print(result)
else:
    print(result - dif)  # 300 - 3 = 297
    
f.close()
