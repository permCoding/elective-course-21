def F(n):
    '''
    вычисляем число Фиббоначи n
    1 1 2 3 5 8 13 21 ... 
    '''
    lst = [0, 1]
    for i in range(2, n+1):
        lst.append(lst[i-1] + lst[i-2])
    return lst


n = 36
print(*F(n)[1:])
