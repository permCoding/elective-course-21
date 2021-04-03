# https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=3776
# делилась на 9 и наименьшая

f = open('27-57a.txt')
lines = f.readlines()
f.close()

n = int(lines[0])
##lst = [int(lines[i+1]) for i in range(n)]
lst = list(map(int, lines[1:]))
smin = 4*10**8
for i1 in range(0, n-3):
    for i2 in range(i1+1, n-2):
        for i3 in range(i2+1, n-1):
            for i4 in range(i3+1, n-0):
                tmp = lst[i1]+lst[i2]+lst[i3]+lst[i4]
                if tmp%9 == 0 and tmp < smin:
                    smin = tmp
print(smin)



