f = open('27-A_demo.txt')
n = int(f.readline())

result = 0
for _ in range(n):
    line = f.readline()
    lst = line.split()
    a = int(lst[0])
    b = int(lst[1])
    result += max(a, b)
    # -=  *=  /=  //=  +=  %=

print(result)
f.close()