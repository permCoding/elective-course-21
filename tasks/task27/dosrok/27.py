f = open('27_A.txt')
n = int(f.readline())
d = 9999
summ = 0
for i in range(n):
    c,b,a = sorted(map(int,f.readline().split()))
    summ += a
    if (a-b)%109!=0 and (a-b)<d:
        d = a-b
    elif (a-c)%109!=0 and (a-c)<d:
        d = a-c
    
if summ%109==0:
    summ -= d

print(summ)


