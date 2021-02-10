'''
Какое максимальное количество идущих подряд символов,
среди которых каждые два соседних различны.
'''
line = 'XYZZXZXYXY' # проверяем строку из всех одинаковых символов
# line += line[-1]

count = 1
max_count = 1
for i in range(len(line)-1):
    if line[i] != line[i+1]:
        count += 1
    else:
        if count > max_count:
            max_count = count
        count = 1

if count > max_count:
            max_count = count

if max_count == 1:
    max_count = 0
    
print(max_count)
