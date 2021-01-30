##f = open('24_demo.txt')
path = r'C:\Users\algop\Documents\GitHub\elective-course-21\py\day08'
file_name = '24_demo.txt'
full_name = path + '/' + file_name
f = open(full_name)
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

print(max_count)
