def get_m(i):
    dmin, dmax = 0, 0
    for j in range(2, i):
        if i%j == 0:
            dmin, dmax = j, i//j
            break 
    return dmin + dmax

cnt = 0
i = 452021
while True:
    i += 1
    m = get_m(i)
    if m%7 == 3:
        cnt += 1
        print(i, m)
    if cnt == 5:
        break
