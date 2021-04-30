# https://kpolyakov.spb.ru/school/ege/gen.php?action=viewVar&answers=on&varId=1
# 2649

f = open('26-s1.txt')
lines = f.read().split('\n')
f.close()

n = int(lines[0])
lst = list(reversed(sorted(map(int, lines[1:n+1]))))

print(n)
print(len(lst))
a = lst[:n//2]
b = lst[n//2:]

print(b[0])

for i in range(0, n//2):
    print(a[i], b[i])
