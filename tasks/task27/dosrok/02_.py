'''
(х → y) \/ ¬( w → z).
zywx
'''
from itertools import product

for x,y,w,z in product([0,1], repeat=4):
                u1 = x<=y
                u2 = not(w<=z)
                u = u1 or u2
                if not (u):
                    print(x,y,w,z)