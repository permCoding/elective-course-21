n = 10000
lst = list(range(n+1))

k = 2
while k<n+1:
    if lst[k] != 0:
        for i in range(k*k,n+1,k):
            lst[i] = 0
    k += 1

print(*list(filter(lambda x: x != 0, lst)))