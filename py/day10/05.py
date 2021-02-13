def F(n):
    '''
    вычисляем число Фиббоначи n
    1 1 2 3 5 8 13 21 ... 
    '''
    lst = [0, 1]
    for i in range(2, n+1):
        lst.append(lst[i-1] + lst[i-2])
    return lst


n = 55
listF = F(n)[1:]
mapS = map(str, listF)
print(mapS)

for item in mapS:
    print(item)

##strF = listF
##print(strF)
