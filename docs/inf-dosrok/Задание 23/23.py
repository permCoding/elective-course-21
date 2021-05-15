def get(y,x):
    if y < x:
        return 0
    if y == x:
        return 1
    return get(y-2,x) + get(y-5,x)
print(get(23,2))
