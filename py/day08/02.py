line = 'XYZZXYX'
# нужно набирать только подряд идущие разные символы
count = 1
for i in range(len(line)-1):
    if line[i] != line[i+1]:
        count += 1
    else:
        count = 1

print(count)
