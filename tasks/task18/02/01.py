f = open('inf_22_10_20_18.txt')
lines = f.readlines()
f.close()

lines = list(map(float, lines))

m = 0
pred = lines[0]
s = pred
for i in range(1, len(lines)):
    if pred > lines[i]:
        s += lines[i]
    else:
        if s > m: m = s
        s = lines[i]
    pred = lines[i]

print(int(m))
