lst = [0, 1]
n = 36
for i in range(2, n+1):
    lst.append(lst[i-1] + lst[i-2])
print(lst[n])

##def F(n):
##    lst = [0, 1, 1]
##        return F(n-2) + F(n-1)
##
##for i in range(1, 37):
##    print(i, F(i))

'''
1 1 2 3 5 8 13 21 ... 
'''
