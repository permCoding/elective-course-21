line = 'XYZYXXYZ' # а что если сначала был отрезок больше, чем потом

count = 1
max_count = 1
for pos in range(len(line)-1):
    if line[pos] != line[pos+1]:
        count += 1
    else:
        count = 1
    max_count = max(max_count, count)

print(max_count)