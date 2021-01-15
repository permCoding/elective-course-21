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

lines = get_lines('table-2.txt')  # читаем второй файл

for line in lines:
    arr = line.split('\t')
    if dct[int(arr[0])][0] == 'Ж':  # проверяем только Ж
        year1 = dct[int(arr[1])][1]
        year0 = dct[int(arr[0])][1]
        r = year1 - year0  # ищем разницу между возрастами
        if r > 22:
            print(r)