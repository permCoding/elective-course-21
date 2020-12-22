f = open('10_demo2021.txt')
s = f.read().lower().split()
f.close()

f = 'долг'
count = 0

for e in s:
    if f in e:
        print(e)
        count += 1

print(count)