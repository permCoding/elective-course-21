lst = []
for n in range(3*10**10, 5*10**10+1, 100000): # u2
    u1 = n%11 == 0
    u3 = n%17 != 0 
    u4 = n%23 != 0
    u5 = n%41 != 0
    u6 = n%103 != 0 
    if u1 and u3 and u4 and u5 and u6:
        lst.append(n)

print(len(lst), min(lst))