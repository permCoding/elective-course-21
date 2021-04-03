lst = []
for n in range(1016, 7937+1):
    u1 = n%3 == 0
    u2 = n%7 != 0
    u3 = n%17 != 0 
    u4 = n%19 != 0 
    u5 = n%27 != 0 
    if u1 and u2 and u3 and u4 and u5:
        lst.append(n)
        
# print(lst)
print(len(lst), max(lst))