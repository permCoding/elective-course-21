# читаем первый файл
# составляем из него словарь пар:
# id: [пол, год]
f = open('table-1.txt')
lines = f.readlines()
f.close()

dict1 = {}
for line in lines:
    lst = line.split('\t')
    dict1[int(lst[0])] = [lst[2], int(lst[3])]  # добавляем пару

# читаем второй файл
# проверяем только Ж
# ищем разницу между возрастами
f = open('table-2.txt')
lines = f.readlines()
f.close()

for line in lines:
    arr = line.split('\t')
    if dict1[int(arr[0])][0] == 'Ж':
        year1 = dict1[int(arr[1])][1]
        year0 = dict1[int(arr[0])][1]
        r = year1 - year0
        if r > 22:
            print(r)
