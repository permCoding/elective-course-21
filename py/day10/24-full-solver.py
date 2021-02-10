f = open('24_demo.txt')
line = f.readline()
f.close()

count = 1
max_count = 1
for i in range(len(line)-1):
    if line[i] != line[i+1]:
        count += 1
        if count > max_count:
            max_count = count
    else:
        count = 1

if max_count == 1: # если все символы одинаковы
    max_count = 0
    
print(max_count)
