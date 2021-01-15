f = open('table-2.txt')
lines = f.readlines()
f.close()

tab2 = []
for line in lines:
    lst = line.split('\t')
    tab2.append([int(lst[0]), int(lst[1])])

for row in tab2:
    print(*row)