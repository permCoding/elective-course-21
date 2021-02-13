def F(n):
    if n == 1 or n == 2: return 1
    return F(n-2) + F(n-1)

print(F(8))

'''
1 1 2 3 5 8 13 21 ... 
'''
