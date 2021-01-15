def get_lines(name_file):
    f = open(name_file)
    lines = f.readlines()
    f.close()
    return lines


def get_dict(lines):
    dct = {}
    for line in lines:
        lst = line.split('\t')
        dct[int(lst[0])] = [lst[2], int(lst[3])]
    return dct


lines = get_lines('table-1.txt')
dct = get_dict(lines)

for key in dct.keys():
    print(key, dct[key])