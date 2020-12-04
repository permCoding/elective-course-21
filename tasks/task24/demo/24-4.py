# нужно брать данные из файла
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

print(max_count)