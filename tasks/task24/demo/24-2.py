# step 2 - добавим сброс счётчика когда пара равных символов

line = 'XYZZYXYZ'

count = 1
for pos in range(len(line)-1):
    if line[pos] != line[pos+1]:
        count += 1
    else:
        count = 1

print(pos)
print(count)