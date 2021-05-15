f = open('24.txt')
s = f.readline()
f.close()
print(max(map(len, s.split('XZZY'))))
