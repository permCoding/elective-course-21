def dl(n, m):
    return not(bool(n%m))


def get(x, A):
    return int(not(dl(x,A))) <= (int(dl(x,6)) <= int(not(dl(x,9))))


for A in range(1, 1000):
    check = True
    for x in range(1, 1000):
        if get(x, A) == False:
            check = False
            break
    if check == True:
        print(A)

print('- - -')

'''
XY R
00 1
01 1
10 0
11 1
'''