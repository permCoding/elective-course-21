# 23
f = open('24.txt')
s = f.readline() + 'XZZY'
f.close()

count = 0
countMax = 0
i = 0
while i < len(s)-3:
    if s[i:i+4] != 'XZZY':
        count += 1
        i += 1
    else:
        countMax = max(count, countMax)
        count = 0
        i += 4

print(countMax)
