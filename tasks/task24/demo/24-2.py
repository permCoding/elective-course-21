line = 'XYZZYXYZ' # добавим сброс счётчика

count = 1
for pos in range(len(line)-1):
    if line[pos] != line[pos+1]:
        count += 1
    else:
        count = 1

print(pos)
print(count)