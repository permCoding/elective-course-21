f = open('test.txt')
line = f.readline()
n = int(line)

for i in range(n):

    #ver1
    #line = f.readline()
    #print(line, end='')

    #ver2
    #line = f.readline()
    #size = len(line)
    #line = line[0:size-1]
    #print(line)

    #ver3
    line = f.readline()[:-1]
    print(line)

f.close()


