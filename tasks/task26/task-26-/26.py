with open('datafull.txt') as f:
    lines = f.readlines()

n,k = map(int, lines[0].split())
lst = [tuple(map(int, line.split())) for line in lines[1:]]
lst = sorted(lst, key=lambda x: (x[1]/x[0], -x[0]))

for i, t in enumerate(lst):
    print(i, t)

print(sum(map(lambda t: t[0], lst[:k])))
print(max(map(lambda t: t[1], lst[:k])))


