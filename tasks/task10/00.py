f = open('10_demo2021.txt')
s = f.read().lower()
f.close()

f = 'долг'
print(s.count(f))

pos = 0
count = 0
while s.find(f, pos):
    b = s.find(f)
    pos = b + len(f)
    count += 1

print(count)