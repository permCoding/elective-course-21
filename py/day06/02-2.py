start = 100
while start > 0:
    
    s = start
    n = 1
    while s < 51:
        s = s + 5
        n = n * 2
    print(start, n)
    
    if n > 64:
        break
    start -= 1