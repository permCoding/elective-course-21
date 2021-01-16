# task 16 demo
def F(n):
    if n == 1:
        return 1
    else:
        if n % 2 == 0:
           return n + F(n - 1)
        else:
            return 2 * F(n - 2) 

print(F(26))

'''
F(n) = 1 при n = 1;
F(n) = n + F(n − 1), если n – чётно,
F(n) = 2 × F(n − 2), если n > 1 и при этом n – нечётно.

'''