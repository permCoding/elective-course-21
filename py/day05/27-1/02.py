f = open('27-A_demo.txt')
n = int(f.readline())

result = 0
for _ in range(n):
    result += max(map(int, f.readline().split()))

print(result)
f.close()
