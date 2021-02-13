def F(n):
    lst = [0, 1]
    for i in range(2, n+1):
        lst.append(lst[i-1] + lst[i-2])
    return lst


n = 8

##listF = F(n)[1:]
##mapS = map(str, listF)
##print('\n'.join(mapS))


##print('\n'.join(list(map(str, F(n)[1:]))))

print('\n'.join(map(str, F(n)[1:])))


##l = ['2', '33', '666']
##print('-*-'.join(l))
