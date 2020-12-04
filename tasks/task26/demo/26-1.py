f = open('26_1.txt', 'r')
s, n = map(int, f.readline().split())

lst = []
for _ in range(n):
    num = int(f.readline())
    lst.append(num)

lst.sort()
# print(lst)

count = 0
size = 0
for i in range(n):
    if size + lst[i] <= s:
        count += 1
        size += lst[i]
    else:
        break

item = lst[count-1]
size -= item
for i in range(count, n):
    if size + lst[i] <= s:
        item = lst[i]
    else:
        break

print(count, item)
