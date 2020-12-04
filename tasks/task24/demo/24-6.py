f = open('24_LDR.txt', 'r')
line = f.readline()
f.close()

count = 0
max_count = 0
for pos in range(len(line)):
    u1 = line[pos] == 'L' and count % 3 == 0
    u2 = line[pos] == 'D' and count % 3 == 1
    u3 = line[pos] == 'R' and count % 3 == 2
    if u1 or u2 or u3:
        count += 1
        max_count = max(max_count, count)
    else:
        count = 1 if line[pos] == 'L' else 0

print(max_count)