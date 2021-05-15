# (х → y) \/ ¬( w → z)

for x in [0,1]:
    for y in [0,1]:
        for w in [0,1]:
            for z in [0,1]:
                a = bool(x <= y)
                b = not(bool(w <= z))
                f = a or b
                if f == False:
                    print(x,y,w,z,f)
