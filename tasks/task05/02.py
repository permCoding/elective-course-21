
n = 0
while True:
    n += 1
    b = bin(n)
    b += str(b.count('1')%2) + '0'
    r = int(b, 2)
    if r > 83:
        print(r)
        break