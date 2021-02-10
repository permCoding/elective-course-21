'''
https://inf-ege.sdamgia.ru/problem?id=27689
Задание 24 - тип 3

'''
f = open('24_27689.txt')
line = f.readline()
f.close()

##line = 'XYXYZXY'
'''
1) счёт нужно вести от начала текущей цепочки
   а не от начала всей строки
2) X - 0, 3, 6, 9
   Y - 1, 4, 7, 10
   Z - 2, 5, 8, 11
'''
count = 0 # X
max_count = 0
for i in range(len(line)):
    u0 = line[i] == 'X' and count % 3 == 0
    u1 = line[i] == 'Y' and count % 3 == 1
    u2 = line[i] == 'Z' and count % 3 == 2
    u3 = line[i] == 'X' and count % 3 != 0
    if u0 or u1 or u2:
        count += 1
        if count > max_count:
            max_count = count
    elif u3:
        count = 1
    else:
        count = 0
    
print(max_count)
