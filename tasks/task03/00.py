t1 = {
    15: 1944,
    22: 1940,
    23: 1968,
    24: 1993,
    32: 1960,
    33: 1987,
    35: 1965,
    42: 1941,
    43: 1955,
    44: 1990,
    46: 2010,
    52: 1995,
    73: 1967
}
t2 = [
    [42,23],
    [73,24],
    [42,32],
    [32,33],
    [32,44],
    [73,52]
]
for item in t2:
    r = t1[item[1]] - t1[item[0]]
    if r > 22:
        print(r)