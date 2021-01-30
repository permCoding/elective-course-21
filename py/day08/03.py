line = 'ZXYXXYZ'
# не обязательно 2-ая цепочка будет длиннее первой
count = 1
max_count = 1
for i in range(len(line)-1):
    if line[i] != line[i+1]:
        count += 1
        if count > max_count:
            max_count = count
    else:
        count = 1

print(max_count)
