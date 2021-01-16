f = open('input.txt')
lines = f.read().split('\n')
f.close()

tab = []
for line in lines:
  lst = line.split('\t')
  tab.append( [int(lst[0]), int(lst[1])] )

# print(tab)

for row in tab:
    print(row[1] - row[0])