for x in range(110203, 110245+1):
    lst = []
    for i in range(1, x+1):
        if i % 2 == 0 and x % i == 0:
            lst.append(i)
    if len(lst) == 4:
        print(*lst)






        
        
