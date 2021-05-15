f = open('26.txt')
line = f.readline()
s, n = map(int, line.split())
lst = []
for i in range(n):
    lst.append(int(f.readline()))
f.close()
lst.sort()

res, k, m, p = 0, 0, lst[-1], lst[-1]
for i in range(len(lst)):
    if res + lst[i] <= s:
        k += 1
        p = lst[i]
        res += lst[i]
    else:
        break

res -= p
for item in lst[::-1]:
    if res + item <= s:
        m = item
        break
print(k, m)
