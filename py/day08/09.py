f = open('test.txt')
lines = f.readlines()
f.close()

n = int(lines[0])

lines = lines[1:]
acc = 0
for line in lines:
    acc += int(line)

print(acc)
