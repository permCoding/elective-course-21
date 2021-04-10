N = 0
while True:
    N += 1
    b = bin(N)
    b += str(b.count('1')%2) + '0'
    R = int(b, 2)
    if R > 43:
        break
print(N, R)