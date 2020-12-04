f = open('26_1.txt', 'r')
s, n = map(int, f.readline().split())

lst = sorted([int(f.readline()) for _ in range(n)])

count, size = 0, 0
for i in range(n):
    if size + lst[i] <= s:
        count += 1
        size += lst[i]

item = lst[count-1]
size -= item
for i in range(count, n):
    if size + lst[i] <= s:
        item = lst[i]

print(count, item)
