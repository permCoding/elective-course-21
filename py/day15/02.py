# (х → y) \/ ¬( w → z)
# (х → y) => x <= y
# z y w x

for x in [0,1]:
    for y in [0,1]:
        for w in [0,1]:
            for z in [0,1]:
                a = x <= y
                b = not(w <= z)
                f = a or b
                if f == False:
                    print(x,y,w,z,f)
