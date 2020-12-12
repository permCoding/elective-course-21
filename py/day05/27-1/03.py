f = open('27-A_demo.txt')
n = int(f.readline())

result = 0
for _ in range(n):
    line = f.readline()
    a, b = map(int, line.split())
    result += max(a, b)
    # % 3

if result % 3 != 0:  # <> не равно
    print(result)
else:
    print()
    
f.close()
