# step 4 - нужно брать данные из файла

f = open('24.txt', 'r')
line = f.readline()
f.close()

count = 1
max_count = 1
for pos in range(len(line)-1):
    if line[pos] != line[pos+1]:
        count += 1
        max_count = max(max_count, count)
    else:
        count = 1

if max_count == 1: max_count = 0 # важно, а что если все были одинаковые
# максимальное количество идущих подряд символов, среди которых каждые два соседних различны
# поэтому max_count не может быть равен 1
print(max_count)
