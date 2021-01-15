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

for key in dict1.keys():
    print(key, dict1[key])