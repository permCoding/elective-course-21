import time

start = time.monotonic()

n = 1000000
lst = list(range(n+1))

k = 2
while k*k < n+1:
    if lst[k] != 0:
        for i in range(k*k,n+1,k):
            lst[i] = 0
    k += 1

finish = time.monotonic()
print(finish-start)

# print(*list(filter(lambda x: x != 0, lst)))
print(len(list(filter(lambda x: x != 0, lst))))
