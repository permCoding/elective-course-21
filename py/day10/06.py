def F(n):
    lst = [0, 1]
    for i in range(2, n+1):
        lst.append(lst[i-1] + lst[i-2])
    return lst


n = 5
listF = F(n)[1:]
mapS = map(str, listF)
print('\n'.join(mapS))





##l = ['2', '33', '666']
##print('-*-'.join(l))
