#x = int(input())
for start in range(500):
    x = start
    Q = 9
    L = 0
    while x >= Q:
        L = L + 1
        x = x - Q
    M = x
    if M < L:
        M = L
        L = x
    if L == 4 and M == 5:
        print(start, L, M)
    # наибольшее
