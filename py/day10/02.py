def F(n):
    if n == 1 or n == 2:
        return 1
    else:
        return F(n-2) + F(n-1)

for i in range(1, 37):
    print(i, F(i))

'''
1 1 2 3 5 8 13 21 ... 
'''
