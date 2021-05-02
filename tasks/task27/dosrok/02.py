'''
(х → y) \/ ¬( w → z).
'''

for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                u1 = x<=y
                u2 = not(w<=z)
                u = u1 or u2
                if not (u):
                    print(x,y,w,z)